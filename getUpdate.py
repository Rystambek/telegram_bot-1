import requests
import os
TOKEN = os.environ['TOKEN']
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def Xabar():
    response = requests.get(url)
    data = response.json()['result'][-1]['message'].keys()
    return data
print(Xabar())