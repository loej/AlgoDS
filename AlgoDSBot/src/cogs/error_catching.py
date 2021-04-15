from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.Cog.listener("on_command_error")
    async def commands_warned(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention}, please send an argument along with your command.")


def setup(AlgoDS):
    AlgoDS.add_cog(Errors(AlgoDS))
