import os
from cogs.utilities import Utilities as util
from discord.ext import commands
from settings import Settings

"""
Settings data from config.json
"""
prefix = Settings('PREFIX').data
discord_token = Settings('DISCORD_TOKEN').data


def setCogs(AlgoDSBot):
    """
    Initializes every Cog file.
    :param AlgoDSBot: AlgoDS Bot object being passed, loads extensions.
    """
    cogs = os.listdir('cogs/')
    for file in cogs:
        if file == '__init__.py' or file == '__pycache__':
            continue
        cog = file.translate({ord(j): None for j in '.py'})
        AlgoDSBot.load_extension("cogs." + cog)


if __name__ == '__main__':
    AlgoDS = commands.Bot(command_prefix=prefix)
    setCogs(AlgoDS)
    AlgoDS.run(discord_token)
