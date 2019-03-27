import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h', '?', ''])
    async def help(ctx, self, catagory : str = None):

        if catagory:
            return

        else:
            return


def setup(bot):
    bot.add_cog(Help(bot))
