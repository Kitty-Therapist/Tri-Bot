import asyncio
import importlib
import discord
import datetime
import json
import os
from subprocess import Popen
import subprocess

from discord.ext import commands
from discord import utils
from utils import Util, Configuration, Permission

class EventSetup:
    def __init__(self, bot):

        async def __local_check(self, ctx):
            return await ctx.bot.is_owner(ctx.author)

    @commands.guild_only()
    @commands.group(hidden=True)
    async def configure(self, ctx: commands.Context):
        """Configure server specific settings."""
        if ctx.subcommand_passed is None:
            await ctx.send("See the subcommands (+help configure) for configurations.")
        
    @configure.command(hidden=True)
    async def submission(self, ctx: commands.Context, channelID):
        """Sets the submission channel."""
        heads = [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
        if ctx.author.id not in heads:
            return

        Configuration.setConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL", channelID)
        await ctx.send(f"The submission channel now is <#{channelID}>")
    
    @configure.command(hidden=True)
    async def modrole(self, ctx: commands.Context, roleID):
        """Sets the role with moderation rights."""
        heads = [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
        if ctx.author.id not in heads:
            return

        Configuration.setConfigVar(ctx.guild.id, "MOD_ROLE_ID", roleID)
        await ctx.send(f"The server moderation role is now `{roleID}`.")

def setup(bot):
    bot.add_cog(EventSetup(bot))
