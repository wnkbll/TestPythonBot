from dotenv import dotenv_values

from src.core.paths import PROD_ENV_PATH

env_values = dotenv_values(PROD_ENV_PATH)

TOKEN = env_values["TOKEN"]
REDIS_URL = env_values["REDIS_URL"]
SOURCE_URL = "https://cbr.ru/scripts/XML_daily.asp"
