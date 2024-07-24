from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
DEV_ENV_PATH = ROOT_DIR.joinpath(".env")
PROD_ENV_PATH = ROOT_DIR.joinpath(".env.prod")
