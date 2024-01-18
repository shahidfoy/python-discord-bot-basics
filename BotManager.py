import asyncio
import discord
import random
from discord.ext import commands
from cogs.DemoCog import AlertCog
from cogs.ModCog import ModeratorRoleCog
from cogs.AdminCog import OwnerCog
import utils.BotUtil as util

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


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
    await bot.process_commands(msg)

@bot.event
async def on_member_join(member):
    print("New member is joining")
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)

    if num == 1:
        await ctx.send("Heads")
    if num == 2:
        await ctx.send("Tails")

@bot.command()
async def rps(ctx, hand):
    hands = ["✌️", "✋", "👊"]
    bothand = random.choice(hands)
    await ctx.send(bothand)

    if hand == bothand:
        await ctx.send("It's a Draw!")
    elif hand == "✌️":
        if bothand == "✋":
            await ctx.send("You won.")
        if bothand == "👊":
            await ctx.send("The bot won.")
    elif hand == "✋":
        if bothand == "👊":
            await ctx.send("You won.")
        if bothand == "✌️":
            await ctx.send("The bot won.")
    elif hand == "👊":
        if bothand == "✋":
            await ctx.send("You won.")
        if bothand == "✌️":
            await ctx.send("The bot won.")

@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands", description = "These are the Commands that you can use for this bot", color = discord.Color.dark_purple())
    MyEmbed.set_thumbnail(url = "https://th.bing.com/th/id/OIG.UmTcTiD5tJbm7V26YTp.?w=270&h=270&c=6&r=0&o=5&pid=ImgGn")
    MyEmbed.add_field(name = "!ping", value = "This command allows you to check if the bot is active.", inline = False)
    MyEmbed.add_field(name = "!coinflip", value = "This command allows you to flip a coin.", inline = False)
    MyEmbed.add_field(name = "!rps", value = "This command allows you to play a game of rock paper scissors with the boot. 👊 = rock, ✋ = paper, ✌️ = scissors", inline = False)
    await ctx.send(embed = MyEmbed)

@bot.command()
@commands.check(util.is_me)
async def unloadAlert(ctx):
    await bot.remove_cog('AlertCog')

@bot.command()
@commands.check(util.is_me)
async def reloadAlert(ctx):
    await bot.add_cog(AlertCog(bot))

@bot.command()
@commands.check(util.is_me)
async def unloadModerator(ctx):
    await bot.remove_cog('ModeratorRoleCog')

@bot.command()
@commands.check(util.is_me)
async def reloadModerator(ctx):
    await bot.add_cog(ModeratorRoleCog(bot))

@bot.command()
@commands.check(util.is_me)
async def unloadOwner(ctx):
    await bot.remove_cog('OwnerCog')

@bot.command()
@commands.check(util.is_me)
async def reloadOwner(ctx):
    await bot.add_cog(OwnerCog(bot))

async def startcog():
   await bot.add_cog(AlertCog(bot))
   await bot.add_cog(ModeratorRoleCog(bot))
   await bot.add_cog(OwnerCog(bot))

asyncio.run(startcog())
bot.run("<BOT-SDK-KEY>")
