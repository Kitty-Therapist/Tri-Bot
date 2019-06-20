import asyncio
import importlib
import datetime
import os
import operator
import json
from subprocess import Popen
import subprocess
import datetime

from discord.ext import commands
from discord import utils
from utils import Util, Configuration

class EventControl(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    @commands.command(hidden=True)
    async def start(self, ctx: commands.Context):
        """Starts the event!"""
        if os.path.exists(f'submissions/{ctx.guild.id}.json') is True:
            return await ctx.send("There is a event already running! Use the event end command before starting a new one.")

        mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        channel = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL")))
        everyone = None

        data = {}
        with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        if ctx.author.id not in mods:
            return

        for role in channel.guild.roles:
            if role.id == channel.guild.id:
                everyone = role
                await channel.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)
        await ctx.send("Event has started!")

    @commands.command(hidden=True)
    async def end(self, ctx:commands.Context):
        """Ends the event!"""
        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            return await ctx.send("There is currently no event running.")   

        mods = discord.utils.get(ctx.guild.roles, id=391357618683379724)
        channel = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL")))
        everyone = None

        if ctx.author.id not in mods:
            return

        for role in channel.guild.roles:
            if role.id == channel.guild.id:
                everyone = role
                await channel.set_permissions(everyone, read_messages=False)
        await ctx.send("Event has ended!")
        os.remove(f'submissions/{ctx.guild.id}.json')

def setup(bot):
    bot.add_cog(EventControl(bot))
