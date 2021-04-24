import requests
from selenium import webdriver
from settings import Settings
from discord.ext import commands
from bs4 import BeautifulSoup as bsp

example_search = requests.get("https://github.com/loej/AlgoDS/blob/master/Algorithms/Java/Java%20-%20Seaching"
                              "/LinearSearch.java")


class CarbonRequests(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @staticmethod
    def request_algorithm(language, concept, algo):
        link = f"https://github.com/loej/AlgoDS/tree/master/Algorithms/{language}/{language}%20-%20{concept}/{algo}.{str(language).lower()} "
        return link

    @commands.command('ec')
    @commands.is_owner()
    async def eval_carbon(self, ctx):
        algorithm = bsp(example_search.content, features='html.parser')
        fining = algorithm.findAll('td', attrs={'class':'blob-code blob-code-inner js-file-line'} )
        content = ''.join([str(code.text) for code in fining])
        content = f"```java{content}```"
        print(content)
        await ctx.send(content)


def setup(AlgoDS):
    AlgoDS.add_cog(CarbonRequests(AlgoDS))
