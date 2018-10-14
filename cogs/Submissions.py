import discord
import re
import asyncio
import os
import json

from discord.ext import commands
from discord.ext.commands import BucketType
from discord import utils
from utils import Configuration, Permission


class Submissions:
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    if not os.path.exists('submissions'):
        os.makedirs('submissions')

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def submit(self, ctx, *content):
        upvote = utils.get(self.bot.emojis, id=499401182427611136)

        if os.path.exists('submissions/currentevent.json') is False:
            return await ctx.send("There is currently no event running.")

        for server in ctx.bot.guilds:
            channel = self.bot.get_channel(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL"))
            if not channel:
                return await ctx.send("The submission channel is not configured on one of the event servers, please tell a moderator immediantly.")

        links = re.findall(r"https?://\S+\.\S+", ' '.join(content))
        if not links or len(links) > 1:
            return await ctx.send("Your submission must contain at least one link, and no more than one!")

        try:
            with open(f'submissions/currentevent.json', 'r') as infile:
                data = json.load(infile)
            if str(ctx.author.id) in data:
                reply = await ctx.send("You already submitted the following: " + data[str(ctx.author.id)]['SUBMISSION_LINK'])
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
                return
            else:
                message_ids = []
                for server in ctx.bot.guilds:
                    channel = self.bot.get_channel(Configuration.getConfigVar(server.id, "SUBMISSION_CHANNEL"))
                    message = await channel.send((
                        f"**Artist:** {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})\n"
                        f"**Link{'s' if len(links) > 1 else ''}:** {' '.join(links)}"
                    ))
                    await message.add_reaction(upvote)
                    message_ids.append(message.id)
                data[str(ctx.author.id)] = {'SUBMISSION_LINK': ', '.join(links), 'MESSAGE_ID' : message_ids, 'VOTES' : 0}
                reply = await ctx.send("I've sent your submission through, good luck with the event!")
                await asyncio.sleep(10)
                await reply.delete()
                await ctx.message.delete()
            with open(f'submissions/currentevent.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        except discord.Forbidden:
            return await ctx.send("I can't send messages to one of the submission channels, please tell a moderator.")


def setup(bot):
    bot.add_cog(Submissions(bot))
