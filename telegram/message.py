from .photo import Photo
from .sticker import Sticker
from .video import Video
class Message:
    def __init__(self,message:dict):
        self.message_id = message['message_id']
        self.from_user = message['from']
        if 'text' in message.keys():
            self.text = message['text']
        if 'photo' in message.keys():
            self.photo = Photo(message['photo'][-1])
        if 'sticker' in message.keys():
            self.sticker = Sticker(message['sticker'])
        if 'video' in message.keys():
            self.photo = Video(message['video'][-1])
