import discord
from discord.ext import commands

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
