import discord
from discord.ext import commands
import asyncio


class BugReports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['bug'])
    async def bugreport(self, ctx):

        gzcolour = discord.Colour.from_rgb(48,59,60)

        bugreporttemplate = "\n\n **Brief description:** \n\n**Steps To Reproduce:** \n\n**Images / Videos:** \n\n**Host or Client:** \n\n**Players in your game:** \n\n**Hardware specifications:** "

        embed = discord.Embed(description = bugreporttemplate, colour=discord.Colour.from_rgb(28, 87, 88))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BugReports(bot))
