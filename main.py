import os 
import telegram
from pprint import pprint
from time import sleep
# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object

bot = telegram.Bot(TOKEN)

# update = bot.getUpdates()
# update_id = update.update_id
# chat_id = update.chat.id
# text = update.message.text

# echo bot 
last_update_id = -1
while True:
    update = bot.getUpdates()
    if update.update_id != last_update_id:
        last_update_id = update.update_id
        chat_id = update.chat.id
        # if 'text' in bot.Updates().keys():
        #     text = update.message.text
        #     bot.sendMessage(chat_id, text)
        if 'photo' in bot.Updates().keys():
            photo = update.message.photo.file_id
            bot.sendPhoto(chat_id,photo)
    sleep(2)
