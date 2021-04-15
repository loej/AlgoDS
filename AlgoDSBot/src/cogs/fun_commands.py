import random
from discord.ext import commands
from settings import Settings

userID = Settings('CREATOR_USER_ID').data

friends = {1: "benry", 2: "edrick", 3: "andres", 4: "bames", 5: "boel", 6: "axel"}
reactions = {1: '🍖', 2: '🤡', 3: '❤'}


class FunCommands(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong'd: {0}".format(round(self.AlgoDS.latency, 5)))

    @commands.Cog.listener('on_message')
    async def friend_reactions(self, message):
        check_friend = message.content.lower()
        if check_friend in friends.values():
            await message.add_reaction(reactions.get(random.randint(1, 3)))



def setup(AlgoDS):
    AlgoDS.add_cog(FunCommands(AlgoDS))
