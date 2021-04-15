from discord.ext import commands
from bs4 import BeautifulSoup as bsp
from settings import Settings


class CarbonRequests(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.command('ec')
    @commands.is_owner()
    async def eval_carbon(self, ctx):
        soup = bsp("<p>joel<b>ok<i>HTML", features='html.parser')
        await ctx.send(soup.find(text="joel"))


def setup(AlgoDS):
    AlgoDS.add_cog(CarbonRequests(AlgoDS))
