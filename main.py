from pyrogram import Client, filters
import requests 


app = Client(
    "droplink",
    bot_token="1846291789:AAEXly1AdedJrCwumyPALDIY4lNvEGnh5-w"
)



api_token = "e0decc69310ffbf915d46649b32fdfe6941a0d73"



@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  await message.reply_text(f"Hello {message .from_user.first_name}\nI am Droplink.co short link genrator.", reply_to_message_id = message.message_id)



@app.on_message(filters.private & filters.regex("http|https"))
async def kuklink(client,message):
  long_url = message.text
  try:
    r = requests.get(f'https://droplink.co/api?api={api_token}&url={long_url}&format=text')
    result = r.text
    print(result)
    await message.reply_text(f"```{result}```", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
app.run()