import json


class Settings:

    def __init__(self, user_request):
        self.user_request = user_request
        self.data = self.open_json_file()
        self.json_tokens = json.loads(self.data)
        self.data = self.get_json_data()

    def open_json_file(self):
        with open('config.json', 'r') as file:
            data = file.read()
        return data

    def get_json_data(self):
        return str(self.json_tokens['{}'.format(self.user_request)])
