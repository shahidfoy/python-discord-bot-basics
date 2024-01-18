import discord
from discord.ext import commands, tasks
from datetime import datetime

class AlertCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "ping alert-cog":
            await msg.channel.send("alert-cog is connected..")

    @commands.command()
    async def pika(self, ctx):
        await ctx.send("chuuu!")

    @commands.command()
    async def pikaimage(self, ctx):
        await ctx.send("pikachu", file=discord.File('./cogs/pika.jpg'))

    @tasks.loop(seconds = 1)
    async def alarm(self, ctx, hour, minute):
        now = datetime.now().time()
        if now.hour == hour and now.minute == minute:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send("pikachu alarm reminding you to catch them all.")
            self.alarm.stop()

    @commands.command()
    async def startalarm(self, ctx, date):
        hour, minute = date.split(":")
        hour = int(hour)
        minute = int(minute)
        self.alarm.start(ctx, hour, minute)
