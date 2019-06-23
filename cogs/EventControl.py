import asyncio
import importlib
import datetime
import os
import operator
import json
import discord
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

        mods = discord.utils.get(ctx.guild.roles, id=591040785114202114)
        fanart = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "FAN_ART_CHANNEL")))
        merch = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MERCH_CHANNEL")))
        emoji = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "EMOJIS_CHANNEL")))
        music = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MUSIC_CHANNEL")))
        story = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "STORY_CHANNEL")))
        productivity = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "PRODUCTIVITY")))
        shitpost = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "SHITPOST")))
        social = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "SOCIAL")))
        moderation = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MODERATION")))
        entertainment = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "ENTERTAINMENT")))        
        everyone = None

        data = {}
        with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        if 591040785114202114 not in [role.id for role in ctx.author.roles]:
            return

        for role in fanart.guild.roles:
            if role.id == fanart.guild.id:
                everyone = role
                await fanart.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in merch.guild.roles:
            if role.id == merch.guild.id:
                everyone = role
                await merch.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in emoji.guild.roles:
            if role.id == emoji.guild.id:
                everyone = role
                await emoji.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in music.guild.roles:
            if role.id == music.guild.id:
                everyone = role
                await music.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in story.guild.roles:
            if role.id == story.guild.id:
                everyone = role
                await story.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in entertainment.guild.roles:
            if role.id == entertainment.guild.id:
                everyone = role
                await entertainment.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in moderation.guild.roles:
            if role.id == moderation.guild.id:
                everyone = role
                await moderation.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in productivity.guild.roles:
            if role.id == productivity.guild.id:
                everyone = role
                await productivity.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in shitpost.guild.roles:
            if role.id == shitpost.guild.id:
                everyone = role
                await shitpost.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)

        for role in social.guild.roles:
            if role.id == social.guild.id:
                everyone = role
                await social.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False)        

        await ctx.send("Event has started!")

    @commands.command(hidden=True)
    async def end(self, ctx:commands.Context):
        """Ends the event!"""
        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            return await ctx.send("There is currently no event running.")   

        mods = discord.utils.get(ctx.guild.roles, id=591040785114202114)
        fanart = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "FAN_ART_CHANNEL")))
        merch = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MERCH_CHANNEL")))
        emoji = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "EMOJIS_CHANNEL")))
        music = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MUSIC_CHANNEL")))
        story = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "STORY_CHANNEL")))
        productivity = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "PRODUCTIVITY")))
        shitpost = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "SHITPOST")))
        social = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "SOCIAL")))
        moderation = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "MODERATION")))
        entertainment = ctx.bot.get_channel(int(Configuration.getConfigVar(ctx.guild.id,  "ENTERTAINMENT")))      
        everyone = None

        if 591040785114202114 not in [role.id for role in ctx.author.roles]:
            return

        for role in fanart.guild.roles:
            if role.id == fanart.guild.id:
                everyone = role
                await fanart.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in merch.guild.roles:
            if role.id == merch.guild.id:
                everyone = role
                await merch.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)
        for role in emoji.guild.roles:
            if role.id == emoji.guild.id:
                everyone = role
                await emoji.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in music.guild.roles:
            if role.id == music.guild.id:
                everyone = role
                await music.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in story.guild.roles:
            if role.id == story.guild.id:
                everyone = role
                await story.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in entertainment.guild.roles:
            if role.id == entertainment.guild.id:
                everyone = role
                await entertainment.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in moderation.guild.roles:
            if role.id == moderation.guild.id:
                everyone = role
                await moderation.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in productivity.guild.roles:
            if role.id == productivity.guild.id:
                everyone = role
                await productivity.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in shitpost.guild.roles:
            if role.id == shitpost.guild.id:
                everyone = role
                await shitpost.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)

        for role in social.guild.roles:
            if role.id == social.guild.id:
                everyone = role
                await social.set_permissions(everyone, read_messages=False, send_messages=False, add_reactions=False)     
        await ctx.send("Event has ended!")
        os.remove(f'submissions/{ctx.guild.id}.json')

    @commands.group()
    async def blacklist(self, ctx:commands.Context):
        """Base command for managing the name blacklist"""
        if ctx.subcommand_passed is None:
            await ctx.send("See the subcommands (+help blacklist) for the blacklist!")

    @blacklist.command()
    async def add(self, ctx, *, word: str):
        """Add a new entry to the list"""
        blacklist = Configuration.getConfigVar(ctx.guild.id, "BAD_LINKS")
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        if word in blacklist:
            await ctx.send("It would appear that this link is already blacklisted.")
        else:
            blacklist.append(word)
            await ctx.send(f"I have added ``{word}`` to the link blacklist!")
            Configuration.setConfigVar(ctx.guild.id, "BAD_LINKS", blacklist)

    @blacklist.command("remove")
    async def blacklist_remove(self, ctx, *, word: str):
        blacklist = Configuration.getConfigVar(ctx.guild.id, "BAD_LINKS")
        mods = discord.utils.get(ctx.guild.roles, id=590955362106998784)
        if 590955362106998784 not in [role.id for role in ctx.author.roles]:
            return
        if word not in blacklist:
            return await ctx.send("I was not able to find this link that was blacklisted.")
        else:
            blacklist.remove(word)
            await ctx.send(f"``{word}`` has been removed from the blacklist.")
            Configuration.setConfigVar(ctx.guild.id, "BAD_LINKS", blacklist)
def setup(bot):
    bot.add_cog(EventControl(bot))
