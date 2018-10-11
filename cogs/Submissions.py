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
from utils import Configuration, Permission

class Submissions:
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    @commands.command()
    async def submit(self, ctx, link):
        channel = ctx.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL"))
        upvote = utils.get(self.bot.emojis, id=499401182427611136)
        if channel != None:
            try:
                message = await channel.send(f"**Artist's Username:** {ctx.author.name}#{ctx.author.discriminator}\n\n**Artist's userID:** {ctx.author.id}\n\n{link}")
                await message.add_reaction(upvote)
                await ctx.send("I've sent your submission through, goodluck with the event!")
            except discord.Forbidden:
                    await ctx.send("I was not able to send to the suggestion channel, make sure I have permissions.")
        else:
            await ctx.send("Either that there is no submission channel, or you are trying to send an empty submission.")

def setup(bot):
    bot.add_cog(Submissions(bot))
