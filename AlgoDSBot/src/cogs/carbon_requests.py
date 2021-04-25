import requests
import json
from selenium import webdriver
from settings import Settings
from cogs.embeds import Embeds
from algo_requests.algorithm_content import Algorithm as Algo
from discord.ext import commands
from bs4 import BeautifulSoup as bsp


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
        algorithm = Algo("Java", "Seaching", "BinarySearch").request_algorithm()

        await ctx.send(algorithm)

    @commands.command('ccA')
    @commands.is_owner()
    async def eval_requests(self, ctx):
        parameters = {
            "code": "123"
        }
        algo_request = requests.get(url="https://carbonnowsh.herokuapp.com/", params=parameters)
        # embed = Embeds.set_algo_embed("title", algo_request.url)
        print(algo_request.status_code)
        print(algo_request.url)
        await ctx.send(embed=Embeds.set_algo_embed("title", algo_request.url))


def setup(AlgoDS):
    AlgoDS.add_cog(CarbonRequests(AlgoDS))
