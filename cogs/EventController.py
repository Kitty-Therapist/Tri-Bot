import asyncio
import importlib
import datetime
import os
from subprocess import Popen
import subprocess

from discord.ext import commands
from discord import utils
from utils import Util, Configuration

class EventControl:
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    @commands.command(hidden=True)
    async def start(self, ctx: commands.Context):
        """Starts the event!"""
        heads = [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
        channel = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL")))
        everyone = None

        if ctx.author.id not in heads:
            return

        for role in channel.guild.roles:
            if role.id == channel.guild.id:
                everyone = role
                await channel.set_permissions(everyone, read_messages=True)
                await ctx.send("Event has started!")

    @commands.command(hidden=True)
    async def end(self, ctx:commands.Context):
        """Ends the event!"""
        heads = [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
        channel = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL")))
        everyone = None

        if ctx.author.id not in heads:
            return

        for role in channel.guild.roles:
            if role.id == channel.guild.id:
                everyone = role
                await channel.set_permissions(everyone, read_messages=False)
                await ctx.send("Event has ended!")

def setup(bot):
    bot.add_cog(EventControl(bot))
