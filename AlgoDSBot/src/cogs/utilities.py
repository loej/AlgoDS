from discord.ext import commands
from settings import Settings
import discord as disc
import json

creator = Settings("CREATOR_USER_ID").data
prefix = Settings("PREFIX").data


class Utilities(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS


    @staticmethod
    def set_embeds(title, subtitle, description):
        url = "https://github.com/loej/AlgoDS"
        embed = disc.Embed(title=title, color=0xFF5733)
        embed.set_author(name="loej", icon_url="https://avatars.githubusercontent.com/u/48299349?v=4")
        embed.set_thumbnail(url="https://raw.githubusercontent.com/loej/AlgoDS/master/Algorithms/other/AlgoDSIcon.png")
        embed.add_field(name=subtitle, value=description, inline=False)
        embed.add_field(name="Contribute", value=f"This project is open source! Feel free to contribute at {url}",
                        inline=True)
        embed.add_field(name="Algorithms", value=f"Use `{prefix}cc algos` to list all of our current algorithms!",
                        inline=True)
        return embed

    @commands.command("about")
    async def about(self, ctx):
        userid = f'<@!{creator}>'
        about_description = f"AlgoDS is a Discord bot made to showcase popular algorithms. It's made by {userid}, an" \
                            f" undergrad CS student at Rutgers University."
        embed = Utilities.set_embeds(f"AlgoDS", "What is this?", about_description)
        await ctx.send(embed=embed)

    @staticmethod
    def get_json_data():
        with open('../config.json', 'r') as file:
            data = json.load(file)
        return data

    @commands.command("setPrefix")
    async def set_prefix(self, ctx, arg):
        passed_prefix = str(arg)
        """
        We need to have a config.json file here
        """
        print(Utilities.get_json_data())

    @commands.command('commands')
    async def send_total_commands(self, ctx):
        total_commands = []
        for coms in self.AlgoDS.commands:
            total_commands.append(f"{coms}")
        main_commands = '\n'.join([str(elem) for elem in total_commands])
        # Have to reformat this
        embed = Utilities.set_embeds("List of commands:", "Current commands", main_commands)
        await ctx.send(embed=embed)


def setup(AlgoDS):
    AlgoDS.add_cog(Utilities(AlgoDS))
