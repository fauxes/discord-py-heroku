import discord
from discord.ext.commands import Bot
from discord.ext import commands
BOT = Bot(command_prefix='alpha')

BOT.run(os.getenv('DISCORD.TOKEN'))
