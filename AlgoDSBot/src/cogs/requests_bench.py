import requests
from discord.ext import commands
import discord as disc


class Requests(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @staticmethod
    def set_embeds(title, subtitle, data, image_option, color):
        embed = disc.Embed(title=title, color=0xFF0000)
        if image_option == 'default':
            embed.set_thumbnail(url="https://raw.githubusercontent.com/loej/AlgoDS/master/Algorithms/other/AlgoDSIcon.png")
        elif image_option == 'kbbq':
            embed.set_thumbnail(url="https://castironpotbbq.com/wp-content/uploads/2019/03/blk-stroke.png")
        if data is None:
            embed.add_field(name=subtitle, value="\u200b", inline=True)
        else:
            embed.add_field(name=subtitle, value=data, inline=True)
        return embed

    @commands.command("check")
    @commands.is_owner()
    async def sync(self, ctx):
        response = requests.get("https://castironpotbbq.com/menu/")
        embed = Requests.set_embeds(f"Request sent to {response.url}", f"Status code: {response.status_code}", None)
        await ctx.send(embed=embed)


def setup(AlgoDS):
    AlgoDS.add_cog(Requests(AlgoDS))
