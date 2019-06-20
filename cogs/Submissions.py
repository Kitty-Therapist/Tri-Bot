import discord
import re
import asyncio
import os
import json

from discord.ext import commands
from discord.ext.commands import BucketType
from discord import utils
from utils import Configuration, Permission


class Submissions(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    if not os.path.exists('submissions'):
        os.makedirs('submissions')

    @commands.guild_only()
    @commands.group(hidden=True)
    async def submit(self, ctx: commands.Context):
        """Configure server specific settings."""
        if ctx.subcommand_passed is None:
            await ctx.send("See the subcommands (+help submit) for the categories!")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def art(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "GENERAL_ART_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Artist:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def fanart(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "FAN_ART_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Artist:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def emoji(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "EMOJIS_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Emoji Artist:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def merch(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "MERCH_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Designer:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def music(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "MUSIC_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Musician:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def story(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "STORY_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Author:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def bot(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "GENERAL_BOT_CHANNEL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Bot Developer:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def functional(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "FUNCTIONAL"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Functional Bot Developer:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def entertainment(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "ENTERTAINMENT"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Enterainment Bot Developer:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")

    @submit.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def shitpost(self, ctx, *content):
        channel = self.bot.get_channel(Configuration.getConfigVar(ctx.guild.id, "SHITPOST"))

        if os.path.exists(f'submissions/{ctx.guild.id}.json') is False:
            data = {}
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)

        if not channel:
            return await ctx.send("The submission channel is not configured, please tell a moderator.")

        links = re.findall(r"https?://\S+\.[^\s>]+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/{ctx.guild.id}.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(5)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message = await channel.send((
                    f"**Shitpost Bot Developer:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                    f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                ))
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links)}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(5)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/{ctx.guild.id}.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to the submission channel, please tell a moderator.")


def setup(bot):
    bot.add_cog(Submissions(bot))