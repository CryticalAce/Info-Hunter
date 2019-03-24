import discord
import asyncio
from discord.ext import commands
import string


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_arp():
        async def predicate(ctx):
            return ctx.author.id == 433169579280302082
        return commands.check(predicate)

    @commands.command(aliases=['s'])
    @is_arp()
    async def status(self, ctx, type: int = 0, *args):
        inp = " ".join(args)
        game = discord.Game(f'{inp}')
        if args:
            if inp == 'clear':
                await self.bot.change_presence(activity=None)
                await ctx.send('Status cleared!')
            else:
                await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=inp, type=type))
                await ctx.send('Status has been set to: {}'.format(game))

def setup(bot):
    bot.add_cog(Main(bot))
