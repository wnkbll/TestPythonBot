from dotenv import dotenv_values

from src.core.paths import ENV_PATH

env_values = dotenv_values(ENV_PATH)

TOKEN = env_values["TOKEN"]
REDIS_URL = env_values["REDIS_URL"]
SOURCE_URL = "https://cbr.ru/scripts/XML_daily.asp"
