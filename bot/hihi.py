import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot

BOT = Bot(command_prefix='alpha')

@BOT.event
async def on_ready():
    await BOT.change_presence(activity=discord.Game(name="Cyberpunk 2077"))
    
BOT.run(os.getenv('DISCORDTOKEN'))
