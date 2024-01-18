import discord
from discord.ext import commands
from datetime import datetime

class ModeratorRoleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "ping moderator-cog":
            await msg.channel.send("moderator-cog is connected..")

    @commands.command()
    @commands.has_role("Moderator")
    async def createrole(self, ctx, *,input):
        await ctx.guild.create_role(name = input)

    @commands.command()
    @commands.has_role("Moderator")
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await ctx.guild.kick(member, reason = reason)


    @commands.command()
    @commands.has_role("Moderator")
    async def mute(self, ctx, user: discord.Member):
        await user.edit(mute = True)

    @commands.command()
    @commands.has_role("Moderator")
    async def unmute(self, ctx, user: discord.Member):
        await user.edit(mute = False)

    @commands.command()
    @commands.has_role("Moderator")
    async def deafen(self, ctx, user: discord.Member):
        await user.edit(deafen = True)

    @commands.command()
    @commands.has_role("Moderator")
    async def undeafen(self, ctx, user: discord.Member):
        await user.edit(deafen = False)

    @commands.command()
    @commands.has_role("Moderator")
    async def voicekick(self, ctx, user: discord.Member):
        await user.edit(voice_channel = None)

    @commands.command()
    @commands.has_role("Moderator")
    async def purge(self, ctx, amount, day : int = None, month : int = None, year = datetime.now().year):
        if amount == "/":
            if day == None or month == None:
                return 
            else:
                await ctx.channel.purge(after = datetime(year, month, day))
        else:
            await ctx.channel.purge(limit = int(amount) + 1)

    @purge.error
    async def errorhandler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You have to specify either a date or a number.")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("You can only have a slash or a number as the first input.")

    @createrole.error
    @kick.error
    @mute.error
    @unmute.error
    @deafen.error
    @undeafen.error
    @voicekick.error
    @purge.error
    async def errorhandler(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("You don't have the necessary role for this command.")
