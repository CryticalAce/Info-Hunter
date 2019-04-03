import discord
import asyncio
from discord.ext import commands
import json
import os
import random

os.chdir(r'C:\Users\jordi\Desktop\GenZeroBot')
users = []

class Ranks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def update(users, user):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['xp'] = 0
            users[user.id]['level'] = 1

    async def add_xp(users, user, exp):
        users[user.id]['xp'] += exp

    async def levelup(users, user, channel):
        xp = users[user.id]['experience']
        clevel = users[user.id]['level']
        nlevel = int(xp ** (1/4))

        if clevel < nlevel:
            await ctx.send(f'Nice {user.mention}, you have leveled up to level {nlevel}')

        users[user.id]['level'] = nlevel

    async def on_member_join(user):
        with open('userdata.json', 'r') as f:
            users = json.load(f)

        await update(users, member)

        with open('userdata.json', 'w') as f:
            json.dump(users, f)

    async def on_message(message):
        with open('userdata.json', 'r') as f:
            users = json.load(f)

        await update(users, ctx.author)
        await add_xp(users, ctx.author, random.randint(10, 20))
        await levelup(users, ctx.author, ctx.channel)

        with open('userdata.json', 'w') as f:
            json.dump(users, f)


def setup(bot):
    bot.add_cog(Ranks(bot))
