import os

import discord
import sys
import sound
import discord
import logging
import subprocess
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
VOICE = os.getenv('DEF_VOICE')

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    activity = discord.Game(name="Use $start to join! ", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Now Accepting Commands")




@bot.command()
async def start(ctx):
    await ctx.channel.send("Starting...")
    subprocess.call([r'\Startup.bat'])



    

bot.run(TOKEN)
