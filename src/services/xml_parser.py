import asyncio
from xml.etree import ElementTree

import aiohttp

from src.core.config import SOURCE_URL
from src.models.currencies import Currency


async def get_currencies() -> list[Currency]:
    async with aiohttp.ClientSession() as session:
        async with session.get(SOURCE_URL) as response:
            xml = await response.text()
            root = ElementTree.fromstring(xml)

            currencies: list[Currency] = []
            for __currency in root:
                dict_currency: dict[str, str | float] = {}
                for param in __currency:
                    if param.tag == "Value" or param.tag == "VunitRate":
                        number = float(param.text.replace(",", "."))
                        dict_currency[param.tag] = number
                    else:
                        dict_currency[param.tag] = param.text

                currencies.append(Currency.model_validate(dict_currency))

            return currencies


asyncio.run(get_currencies())
