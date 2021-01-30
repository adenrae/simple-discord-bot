import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    #for guild in client.guilds:
     #   if guild.name == GUILD:
      #      break
    
    print (
        f'{bot.user.name} is connected to Discord!'
        #f'{guild.name}(id: {guild.id})\n'
    )

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

bot.run(TOKEN)