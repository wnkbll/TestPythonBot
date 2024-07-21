from aiogram import Router, types
from aiogram.filters import Command, CommandObject

from src.db.db_redis import get_currencies

router = Router()


@router.message(Command("exchange"))
async def exchange(
        message: types.Message,
        command: CommandObject,
) -> None:
    args = command.args

    if args is None:
        await message.answer("Неверные параметры.")
        return

    args = command.args.split(" ")

    if len(args) != 3:
        await message.answer("Неверные параметры.")
        return

    currencies = await get_currencies()

    dict_currencies = {
        currency.CharCode: currency.VunitRate for currency in currencies
    }
    dict_currencies["RUB"] = 1

    codes = dict_currencies.keys()

    if any((args[0] not in codes, args[1] not in codes)):
        await message.answer("Неверные параметры.")
        return

    try:
        count = float(args[2])
    except ValueError:
        await message.answer("Неверные параметры.")
        return

    answer = (count * dict_currencies[args[0]]) / dict_currencies[args[1]]

    await message.answer(f"{args[2]} {args[0]} = {answer} {args[1]}")


@router.message(Command("rates"))
async def rates(
        message: types.Message,
) -> None:
    currencies = await get_currencies()

    currencies_middle = int(len(currencies) / 2)

    answer = ""
    for i in range(currencies_middle):
        currency = currencies[i]
        answer += (
            f"Валюта: {currency.CharCode}\n"
            f"\tЦифровой код: {currency.NumCode}\n"
            f"\tНоминал: {currency.Nominal}\n"
            f"\tИмя: {currency.Name}\n"
            f"\tЦена: {currency.Value}\n"
            f"\tКурс(руб. за единицу): {currency.VunitRate}\n"
        )

    await message.answer(
        f"```Currencies 1 / 2:\n{answer}```", parse_mode="Markdown"
    )

    answer = ""
    for i in range(currencies_middle, len(currencies)):
        currency = currencies[i]
        answer += (
            f"Валюта: {currency.CharCode}\n"
            f"\tЦифровой код: {currency.NumCode}\n"
            f"\tНоминал: {currency.Nominal}\n"
            f"\tИмя: {currency.Name}\n"
            f"\tЦена: {currency.Value}\n"
            f"\tКурс(руб. за единицу): {currency.VunitRate}\n"
        )

    await message.answer(
        f"```Currencies 2 / 2:\n{answer}```", parse_mode="Markdown"
    )
