import asyncio
import importlib
import datetime
import os
import json
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
        everyone = None

        if ctx.author.id not in heads:
            return

        for server in ctx.bot.guilds:
            channel = ctx.bot.get_channel(int(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL")))
            if channel is None:
                return await ctx.send("One of the event guilds do not have a submission channel set or the submission channel was deleted!")
        
        if os.path.exists('submissions/currentevent.json') is True:
            return await ctx.send("There is a event already running! Use the event end command before starting a new one.")

        data = {}
        with open('submissions/currentevent.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        for server in ctx.bot.guilds:
            channel = ctx.bot.get_channel(int(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL")))
            for role in channel.guild.roles:
                if role.id == channel.guild.id:
                    everyone = role
                    await channel.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)
        await ctx.send("Event has started!")

    @commands.command(hidden=True)
    async def end(self, ctx:commands.Context):
        """Ends the event!"""
        heads = [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
        everyone = None
  
        if ctx.author.id not in heads:
            return

        for server in ctx.bot.guilds:
            channel = ctx.bot.get_channel(int(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL")))
            if channel is None:
                return await ctx.send("One of the event guilds do not have a submission channel set or the submission channel was deleted!")

        if os.path.exists('submissions/currentevent.json') is False:
            return await ctx.send("There is currently no event running.")   

        os.remove('submissions/currentevent.json')

        for ctx.server in bot.guilds:
            channel = ctx.bot.get_channel(int(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL")))
            for role in channel.guild.roles:
                if role.id == channel.guild.id:
                    everyone = role
                    await channel.set_permissions(everyone, read_messages=False)
        await ctx.send("Event has ended!")

def setup(bot):
    bot.add_cog(EventControl(bot))
