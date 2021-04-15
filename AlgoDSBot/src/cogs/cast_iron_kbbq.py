from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from cogs.embeds import Embeds
import random

cast_iron_pot = requests.get("https://castironpotbbq.com/menu/")


class Kbbq(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.command("kbbq")
    @commands.is_owner()
    async def test_connection(self, ctx):
        embed = Embeds.set_embeds(f"Request sent to {cast_iron_pot.url}", f"Status code: {cast_iron_pot.status_code}",
                                  None, 'default')
        await ctx.send(embed=embed)

    @commands.command("kcontent")
    @commands.is_owner()
    async def getContent(self, ctx, ):
        content = BeautifulSoup(cast_iron_pot.content, 'html5lib')
        finding_all = content.findAll('figcaption', attrs={'class': 'widget-image-caption wp-caption-text'})
        returned_food = '\n'.join([str(element.text) for element in finding_all])
        await ctx.send(returned_food)

    @commands.command('orderKbbq')
    async def order_kbbq(self, ctx):
        menu = BeautifulSoup(cast_iron_pot.content, 'html5lib')
        find_items = menu.findAll('figcaption', attrs={'class': 'widget-image-caption wp-caption-text'})

        kbbq_items = {}
        returned_items = []
        key = 0

        # Setting up our dictionary
        for menu_item in find_items:
            kbbq_items.update({key: menu_item.text})
            key += 1

        #  Choosing 5 random items
        while len(returned_items) < 5:
            choice = kbbq_items.get(random.randint(0, len(kbbq_items) - 1))
            if choice not in returned_items:
                returned_items.append(choice)

        data = "\n".join([str(element) for element in returned_items])
        embed = Embeds.set_embeds("Cast Iron Pot - Orders:", "Randomly Picked Orders", data, 'kbbq')
        await ctx.send(embed=embed)


def setup(AlgoDS):
    AlgoDS.add_cog(Kbbq(AlgoDS))
