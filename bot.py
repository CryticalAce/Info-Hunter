import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTU4NjA1MzA3MDk0MzY4MjY3.D3ZRYA.Xee2ghCqvbrLyA2Q-MtRtwzby3E'

bot = commands.Bot(command_prefix='.',
    description='Custom Generation Zero Bot',
    case_insensitive=True
)

#cogs to load on the initial load of the bot
extensions = ['cogs.main','cogs.wiki', 'cogs.fun']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(f'{extension} could not be loaded! [{error}]')

@bot.event
async def on_ready():
    print(f'Bot is ready [{bot.user}]')
    await bot.change_presence(activity=discord.Activity(name='the server', type=3))

#@bot.event
#async def on_resumed():
#    print('Bot has reconnected')
#    channel = bot.get_channel()
#    await channel.send('Bot has reconnected')

#Load cogs whilst the bot is running
@bot.command(pass_context=True, aliases=['lc'])
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print(f'{extension} loaded')
        await ctx.send(f'{extension} loaded')
    except Exception as error:
        print(f'{extension} could not be loaded! [{error}]')
        await ctx.send(f'{extension} could not be loaded [{error}]')

#Unload cogs whilst the bot is running
@bot.command(pass_context=True, aliases=['ulc'])
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print(f'{extension} unloaded')
        await ctx.send(f'{extension} unloaded')
    except Exception as error:
        print(f'{extenstion} could not be unloaded [{error}]')
        await ctx.send(f'{extension} could not be unloaded [{error}]')

#Reload cogs whilst the bot is running(Good for updates)
@bot.command(pass_context=True, aliases=['rlc'])
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print(f'{extension} unloaded')
    except Exception as error:
        print(f'{extension} could not be unloaded [{error}]')
        await ctx.send(f'{extension} could not be unloaded [{error}]')

    try:
        bot.load_extension(extension)
        print(f'{extension} reloaded')
        await ctx.send(f'{extension} reloaded')
    except Exception as error:
        print(f'{extension} could not be reloaded [{error}]')
        await ctx.send(f'{extension} could not be reloaded [{error}]')

bot.run(TOKEN, reconnect=True)
