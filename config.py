import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    TG_BOT_TOKEN = "1846291789:AAEXly1AdedJrCwumyPALDIY4lNvEGnh5-w"
    APP_ID = "4745045"
    API_HASH = "0156641a61f554d57b41621a1c62fdf9"



def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
