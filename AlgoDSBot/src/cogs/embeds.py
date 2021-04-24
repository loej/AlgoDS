import discord as disc
from discord.ext import commands


class Embeds(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @staticmethod
    def set_embeds(title, subtitle, data, image_option, alt_image=None):
        embed = disc.Embed(title=title, color=0xFF0000)
        if image_option == 'default':
            embed.set_thumbnail(
                url="https://raw.githubusercontent.com/loej/AlgoDS/master/Algorithms/other/AlgoDSIcon.png")
        elif image_option == 'kbbq':
            embed.set_thumbnail(url="https://castironpotbbq.com/wp-content/uploads/2019/03/blk-stroke.png")
            embed.add_field(name="All you can eat Korean BBQ.", value="Dinner $24.95 per person for the good stuff!",
                            inline=False)
            if alt_image is not None:
                embed.set_image(url=alt_image)
        if data is None:
            embed.add_field(name=subtitle, value="\u200b", inline=True)
        else:
            embed.add_field(name=subtitle, value=data, inline=True)
        return embed


def setup(AlgoDS):
    AlgoDS.add_cog(Embeds(AlgoDS))
