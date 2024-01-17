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

@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello python bot":
            await msg.channel.send("hello " + username)

@bot.event
async def on_member_join(member):
    print("New member is joining")
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")

bot.run("<BOT-SDK-KEY>")
