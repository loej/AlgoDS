import discord
import random
from discord.ext import commands
import discord as disc
from settings import Settings

"""
Instructors 
"""
instructors = {1: "Sesh",
               2: "Ames",
               3: "Cowan",
               4: "Joel"}

creatorID = Settings('CREATOR_USER_ID').data


class MainCogs(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print \
            (f'Logged in as: {self.AlgoDS.user.name}\nAlgoDS ID: {self.AlgoDS.user.id}'
             f'\nDiscord Version Info.: \n{discord.version_info}\n{discord.__version__}')
        play_with = instructors.get(random.randint(1, 3))
        await self.AlgoDS.change_presence(status=discord.Status.dnd,
                                          activity=discord.Game(name=f'algos with {play_with}'))
        print(f'Running...\n')

    @commands.Cog.listener('on_message')
    async def print_message(self, message):
        print('Author {0.author} sent: {0.content}'.format(message))

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx):
        await ctx.send(f"You're the only one that can active this, {ctx.author.mention}")


def setup(AlgoDS):
    AlgoDS.add_cog(MainCogs(AlgoDS))
