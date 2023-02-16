import requests
from .message import Message
from .update import Update
from .photo import Photo
from pprint import pprint

class Bot:
    def __init__(self,token:str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}/"

    def getMe(self):
        """
        A simple method for testing your bot's auth token. Requires no parameters. 
        Returns basic information about the bot in form of a User object.
        """
        url = f'{self.base_url}getMe'
        # Requesting the url
        response = requests.get(url)
        # Converting the response to json
        response = response.json()
        # Returning the response
        return response

    def sendMessage(self,chat_id:int,text:str):
        """
        Use this method to send text messages. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            text: Text of the message to be sent
        returns:
            A message object
        """
        # Defining the url to send the message
        url = f'{self.base_url}sendMessage'
        # Defining the data to send
        data = {
            'chat_id':chat_id,
            'text':text
        }
        # Sending the message
        response = requests.post(url,data=data)
        # Converting the response to json
        response = response.json()
        # Converting the response to a message object
        message = Message(response['result'])
        return message

    def getUpdates(self,offset:int=None):
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.
        args:
            offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
        returns:
            An array of update objects
        """
        url = f'{self.base_url}getUpdates'
        response = requests.get(url)
        data = response.json()
        update = Update(data['result'][-1])
        return update

    def sendPhoto(self,chat_id:int,photo:str):
        """
        Use this method to send photos. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data.
        returns:
            A message object
        """
        url = f'{self.base_url}sendPhoto'
        data = {
            'chat_id':chat_id,
            'photo':photo
        }

        response = requests.post(url=url, data=data)
        response = response.json()

        return data


    def sendSticker(self,chat_id:int,sticker:str):
        """
        Use this method to send .webp stickers. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            sticker: Sticker to send. Pass a file_id as String to send a sticker that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .webp file from the Internet, or upload a new one using multipart/form-data.
        returns:
            A message object
        """
        pass

    def sendDocument(self,chat_id:int,document:str):
        """
        Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data.
        returns:
            A message object
        """
        pass

    def sendVideo(self,chat_id:int,video:str):
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video file using multipart/form-data.
        returns:
            A message object
        """
        pass

    def sendLocation(self,chat_id:int,latitude:float,longitude:float):
        """
        Use this method to send point on the map. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            latitude: Latitude of location
            longitude: Longitude of location
        returns:
            A message object
        """
        pass

    def sendContact(self,chat_id:int,phone_number:str,first_name:str):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.
        args:
            chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
            phone_number: Contact's phone number
            first_name: Contact's first name
        returns:
            A message object
        """
        pass

    


