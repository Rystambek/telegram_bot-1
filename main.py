import os 
import telegram
# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object

bot = telegram.Bot(TOKEN)

print(type(bot))