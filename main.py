import os 
import telegram
from pprint import pprint
from time import sleep
from getUpdate import Xabar
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
        data = Xabar()
        print(data)
        if 'text' in Xabar():
            text = update.message.text
            bot.sendMessage(chat_id, text)
        # elif 'photo' in Xabar():
        #     photo = update.message.photo.file_id
        #     bot.sendPhoto(chat_id,photo)
        elif 'sticker' in Xabar():
            sticker = update.message.sticker.file_id
            bot.sendSticker(chat_id,sticker)
        # elif 'video' in Xabar():
        #     sticker = update.message.sticker.file_id
        #     bot.sendSticker(chat_id,sticker)
    sleep(2)
