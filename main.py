from pyrogram import Client, filters
import requests 
import os
from pyrogram import Client
from config import Config
from config import LOGGER

class Bot(Client):
    def __init__(self):
        super().__init__(
            "mybot",
            bot_token=Config.TG_BOT_TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            plugins={
                "root": "plugins"
            },
        )
        self.LOGGER = LOGGER

api_token = "e0decc69310ffbf915d46649b32fdfe6941a0d73"



@Bot.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  await message.reply_text(f"Hello {message .from_user.first_name}\nI am Droplink.co short link genrator.", reply_to_message_id = message.message_id)



@Bot.on_message(filters.private & filters.regex("http|https"))
async def kuklink(client,message):
  long_url = message.text
  try:
    r = requests.get(f'https://droplink.co/api?api={api_token}&url={long_url}&format=text')
    result = r.text
    print(result)
    await message.reply_text(f"```{result}```", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
Bot.run()
