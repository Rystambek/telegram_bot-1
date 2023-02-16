from .photo import Photo
class Message:
    def __init__(self,message:dict):
        self.message_id = message['message_id']
        self.from_user = message['from']
        if 'text' in message.keys():
            self.text = message['text']
        elif 'photo' in message.keys():
            self.photo = Photo(message['photo'][-1])