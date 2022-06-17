import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")



def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
