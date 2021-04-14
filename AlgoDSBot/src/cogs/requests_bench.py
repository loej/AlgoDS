import requests
import json
from discord.ext import commands
import discord as disc


class Requests(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @staticmethod
    def set_embeds(title, subtitle, data):
        embed = disc.Embed(title=title)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/loej/AlgoDS/master/Algorithms/other/AlgoDSIcon.png")
        if data is None:
            embed.add_field(name=subtitle, value="\u200b", inline=True)
        else:
            embed.add_field(name=subtitle, value=data, inline=True)
        return embed

    @commands.command("check")
    @commands.is_owner()
    async def sync(self, ctx):
        response = requests.get("https://carbon.now.sh/")
        embed = Requests.set_embeds(f"Request sent to {response.url}", f"Status code: {response.status_code}", None)
        await ctx.send(embed=embed)


def setup(AlgoDS):
    AlgoDS.add_cog(Requests(AlgoDS))
