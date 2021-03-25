import discord
import json


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    @classmethod
    def open_json_file(cls):
        with open('config.json', 'r') as file:
            data = file.read()
        return data


if __name__ == '__main__':
    class_data = MyClient()
    data = class_data.open_json_file()
    token = json.loads(data)
    client = MyClient()
    client.run(str(token['DISCORD_TOKEN']))
