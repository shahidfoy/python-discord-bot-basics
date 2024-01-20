import discord
from discord.ext import commands
import utils.BotUtil as util

class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "ping owner-cog":
            await msg.channel.send("owner-cog is connected..")

    @commands.command()
    @commands.check(util.is_me)
    async def servername(self, ctx, *,input):
        await ctx.guild.edit(name = input)

    @commands.command()
    @commands.check(util.is_me)
    async def region(self, ctx, *,input):
        await ctx.guild.edit(region = input)

    @region.error
    async def errorhandler(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Please enter a valid region name.")

    @commands.command()
    @commands.check(util.is_me)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        await ctx.guild.ban(member, reason = reason)

    @commands.command()
    @commands.check(util.is_me)
    async def unban(self, ctx, *, input):
        async for entry in ctx.guild.bans():
            username = entry.user.name
            if input == username:
                await ctx.guild.unban(entry.user)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def createtextchannel(self, ctx, *,input):
        await ctx.guild.create_text_channel(name = input)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def createvoicechannel(self, ctx, *,input):
        await ctx.guild.create_voice_channel(name = input)