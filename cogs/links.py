import discord
import asyncio
from discord.ext import commands
import string
import requests
from bs4 import BeautifulSoup
from lxml import html
from difflib import SequenceMatcher

#Global Variables
matches = []
wikipages = ["Dalahäst", "Gnomes", "Trädgårdstomte", "Mixtapes"]

#============== DON'T TOUCH THIS IMPORTS ALL THE PAGE NAMES FROM THE WIKI ==================#
url = requests.get('https://generation-zero.fandom.com/wiki/Special:AllPages').text
soup = BeautifulSoup(url, 'lxml')

My_table = soup.find('table',{'class':'mw-allpages-table-chunk'})

pages = My_table.findAll('a')

for page in pages:
    wikipages.append(page.get('title'))

#============================================================================================#

#Want to use a Similarity Metric and get a score of .5 or above to match

#        page = page.replace('To', 'to').replace('Of', 'of').replace('44', '.44').replace('Magnus', '.44 Magnus').replace('Smg', 'SMG').replace('M46', 'M/46').replace('Kpist', '"Kpist"').replace('Shotgun', 'Pump Action').replace('Automatgevar', 'Automatgevär').replace('Moller', 'Möller').replace('Pp', 'PP').replace('Mixtapes', 'Collectables/Mixtapes').replace('Gnome', 'Gnomes').replace('Gnomes', 'Collectables/Gnomes').replace('Collectables/Gnomess', 'Collectables/Gnomes').replace('Dalahast', 'Dalahäst').replace('Dalahäst', 'Collectables/Dalahäst')

def matcher(inp):
    global wikipages
    global matches

    for page in wikipages:
        ratio = SequenceMatcher(None, inp, page).ratio()
        if ratio <= 0.5:
            next
        elif ratio >=0.51:
            matches.append(page)

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wiki(self, ctx, *, args : str = None):
        global wikipages
        global matches

        if args is None:
            await ctx.send('https://generation-zero.fandom.com')

        elif args:
            matcher(args)

            if len(matches) == 1:
                page = matches[0]
                page = page.replace(" ", "_")

                if page == "Dalahäst" or "Gnomes" or "Mixtapes":
                    page = "Collectables/{0}".format(page)
                await ctx.send(f"https://generation-zero.fandom.com/wiki/{page}")

            elif len(matches) == 0:
                await ctx.send('The page you are seeking could not be found, please check your spelling and try again')

            matches.clear()



def setup(bot):
    bot.add_cog(Main(bot))
