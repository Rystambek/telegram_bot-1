class User:
    def __init__(self, data: dict):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data.get('last_name')
        self.username = data.get('username')
        self.language_code = data.get('language_code')