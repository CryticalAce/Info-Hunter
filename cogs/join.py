import discord
import asyncio
from discord.ext import commands

class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #Getting opinions first

def setup(bot):
    bot.add_cog(Join(bot))