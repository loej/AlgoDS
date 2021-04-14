from discord.ext import commands
from settings import Settings


class CarbonRequests(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS


def setup(AlgoDS):
    AlgoDS.add_cog(CarbonRequests(AlgoDS))
