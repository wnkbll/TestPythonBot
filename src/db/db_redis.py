from loguru import logger
from pydantic import TypeAdapter
from redis import asyncio as aioredis

from src.core.config import REDIS_URL
from src.models.currencies import Currency
from src.services import xml_parser

CODES = [
    "AUD", "AZN", "GBP", "AMD",
    "BYN", "BGN", "BRL", "HUF",
    "VND", "HKD", "GEL", "DKK",
    "AED", "USD", "EUR", "EGP",
    "INR", "IDR", "KZT", "CAD",
    "QAR", "KGS", "CNY", "MDL",
    "NZD", "NOK", "PLN", "RON",
    "XDR", "SGD", "TJS", "THB",
    "TRY", "TMT", "UZS", "UAH",
    "CZK", "SEK", "CHF", "RSD",
    "ZAR", "KRW", "JPY",
]


async def set_currencies() -> None:
    redis = aioredis.from_url(REDIS_URL)
    currencies = await xml_parser.get_currencies()

    type_adapter = TypeAdapter(Currency)
    async with redis.client() as conn:
        for currency in currencies:
            encoded = type_adapter.dump_json(currency).decode("utf-8")
            await conn.set(currency.CharCode, encoded)

    logger.success("Currencies info was successfully updated.")


async def get_currency(char_code: str) -> Currency:
    redis = aioredis.from_url(REDIS_URL)

    type_adapter = TypeAdapter(Currency)

    async with redis.client() as conn:
        encoded = await conn.get(char_code)
        return type_adapter.validate_json(encoded)


async def get_currencies() -> list[Currency]:
    currencies = []
    for code in CODES:
        currencies.append(await get_currency(code))

    return currencies
