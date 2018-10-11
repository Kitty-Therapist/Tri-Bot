import asyncio
import importlib
import discord
import datetime
import json
import os
import re
from subprocess import Popen
import subprocess

from discord.ext import commands
from discord import utils
from utils import Util, Configuration, Permission

class Submissions:
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self.upvote = utils.get(bot.emojis, id=499401182427611136)

    @commands.command()
    async def submit(self, ctx, *content):
        channel = self.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL")))
        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.\S+", ' '.join(content))
        if not links or len(links) > 5:
            return await ctx.send("Your submission must contain at least one link, and no more than five!")

        try:
            message = await channel.send((
                f"**Artist:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
            ))
            await message.add_reaction(self.upvote)
            return await ctx.send("I've sent your submission through, good luck with the event!")
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

def setup(bot):
    bot.add_cog(Submissions(bot))
