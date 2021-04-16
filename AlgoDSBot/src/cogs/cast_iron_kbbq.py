import requests
import random
from bs4 import BeautifulSoup
from cogs.embeds import Embeds
from discord.ext import commands

cast_iron_pot = requests.get("https://castironpotbbq.com/menu/")
cast_iron_images = requests.get("https://castironpotbbq.com/gallery/")


class Kbbq(commands.Cog):

    def __init__(self, AlgoDS):
        self.AlgoDS = AlgoDS

    @commands.command("kbbqStatus")
    @commands.is_owner()
    async def test_connection(self, ctx):
        embed = Embeds.set_embeds(f"Request sent to {cast_iron_pot.url}", f"Status code: {cast_iron_pot.status_code}",
                                  None, 'default')
        await ctx.send(embed=embed)

    @commands.command("menu")
    @commands.is_owner()
    async def getContent(self, ctx, ):
        content = BeautifulSoup(cast_iron_pot.content, 'html5lib')
        finding_all = content.findAll('figcaption', attrs={'class': 'widget-image-caption wp-caption-text'})
        returned_food = '\n'.join([str(element.text) for element in finding_all])
        await ctx.send(returned_food)

    @commands.command('kbbq')
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

    @commands.command("showKbbq")
    async def get_kbbq_images(self, ctx):
        images = BeautifulSoup(cast_iron_images.content, 'html5lib')
        find_images = images.findAll('img', attrs={'class': 'attachment-post-thumbnail size-post-thumbnail'})
        valid_images = ['uploads/2020/09/o-2-370x265.jpg', 'uploads/2020/09/o-370x265.jpg',
                        'uploads/2020/09/o-8-370x265.jpg', 'uploads/2020/09/o-7-370x265.jpg',
                        'uploads/2020/09/o-5-370x265.jpg']
        # Getting the images and slicing the string
        main_pic = ''
        for food_image in find_images:
            url = food_image.attrs['src']
            url = url[38:len(url)]
            url = str(url)
            if url in valid_images:
                choose = random.choice(valid_images)
                main_pic = 'https://castironpotbbq.com/wp-content/'+choose
        print(main_pic)
        pass


def setup(AlgoDS):
    AlgoDS.add_cog(Kbbq(AlgoDS))
