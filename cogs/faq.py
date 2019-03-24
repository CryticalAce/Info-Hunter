import discord
import asyncio
from discord.ext import commands

class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #Listen to and respond to commands

def setup(bot):
    bot.add_cog(FAQ(bot))
