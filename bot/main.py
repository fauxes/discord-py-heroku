import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot

BOT = Bot(command_prefix='alpha')

@BOT.event
async def on_ready():
    await BOT.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="🥚🐣"))
    
BOT.run(os.getenv('DISCORD_TOKEN'))
