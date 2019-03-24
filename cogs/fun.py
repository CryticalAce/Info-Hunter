import discord
from discord.ext import commands
import asyncio
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cookie(self, ctx):
        numCookies = random.randint(0, 12)
        member = ctx.author

        if numCookies == 1:
            await ctx.send(member.mention + f' here is 1 cookie for you :cookie:')

        elif numCookies >= 2:
            await ctx.send(member.mention + f' here are {numCookies} for you ' + numCookies * (':cookie:'))

        else:
            await ctx.send(member.mention + f' no cookies for you but here is a tick instead :tick:')



def setup(bot):
    bot.add_cog(Fun(bot))
