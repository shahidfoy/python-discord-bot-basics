import discord
import random
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
bot_client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print("Bot is online..")

bot.run("<BOT-SDK-KEY>")
