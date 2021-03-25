import discord
import asyncio
from settings import Settings

prefix = Settings('PREFIX').data
discord_token = Settings('DISCORD_TOKEN').data
userID = Settings('CREATOR_USER_ID').data


class Client(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def prefix_commands(self, message):
        if message.content.startswith('{}about'.format(prefix)):
            await message.channel.send('About:')


if __name__ == '__main__':
    AlgoDS = Client()
    AlgoDS.run(discord_token)
