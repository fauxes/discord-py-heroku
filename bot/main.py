import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot

BOT = Bot(command_prefix='alpha')

@BOT.event
async def on_ready():
    await BOT.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Donate to Ukraine!"))
    await BOT.change_presence(activity = discord.Game("Donate to help Ukraine crisis! https://donate.redcross.org.uk/appeal/ukraine-crisis-appeal")) 
    
BOT.run(os.getenv('DISCORD_TOKEN'))
