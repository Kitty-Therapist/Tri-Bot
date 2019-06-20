import asyncio
import datetime
import discord
import configparser
import datetime
import time
import math
import os
import traceback

from discord.abc import PrivateChannel
from discord.ext import commands
from discord import utils
from utils import Configuration, Util, BugLog

if not os.path.exists('config'):
    os.makedirs('config')
    
if not os.path.exists('submissions'):
    os.makedirs('submissions')

TOKEN = "hello token"

bot = commands.Bot(command_prefix = "+")

bot.starttime = datetime.datetime.now()
bot.startup_done = False

initial_extensions = ['EventSetup', 'Reload', 'EventControl']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(f"cogs.{extension}")

@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send("This command cannot be used in private messages.")
    elif isinstance(error, commands.BotMissingPermissions):
        BugLog.error(f"Encountered a permissions error while executing {ctx.command}.")
        await ctx.send(error)
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send("Sorry. This command is disabled and cannot be used.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(error)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"You are missing a required argument! (See {ctx.prefix}help {ctx.command.qualified_name} for info on how to use this command).")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f"Invalid argument given! (See {ctx.prefix}help {ctx.command.qualified_name} for info on how to use this commmand).")
    elif isinstance(error, commands.CommandNotFound):
        return
    else:
        await ctx.send(":rotating_light: Something went wrong while executing that command. :rotating_light:")
        # log to logger first just in case botlog logging fails as well
        BugLog.exception(f"Command execution failed:"
                                f"    Command: {ctx.command}"
                                f"    Message: {ctx.message.content}"
                                f"    Channel: {'Private Message' if isinstance(ctx.channel, PrivateChannel) else ctx.channel.name}"
                                f"    Sender: {ctx.author.name}#{ctx.author.discriminator}"
                                f"    Exception: {error}", error)

        embed = discord.Embed(colour=discord.Colour(0xff0000),
                            timestamp=datetime.datetime.utcfromtimestamp(time.time()))

        embed.set_author(name="Command execution failed:")
        embed.add_field(name="Command", value=ctx.command)
        embed.add_field(name="Original message", value=ctx.message.content)
        embed.add_field(name="Channel", value='Private Message' if isinstance(ctx.channel, PrivateChannel) else ctx.channel.name)
        embed.add_field(name="Sender", value=f"{ctx.author.name}#{ctx.author.discriminator}")
        embed.add_field(name="Exception", value=error)
        v = ""
        for line in traceback.format_tb(error.__traceback__):
            if len(v) + len(line) > 1024:
                embed.add_field(name="Stacktrace", value=v)
                v = ""
            v = f"{v}\n{line}"
        if len(v) > 0:
            embed.add_field(name="Stacktrace", value=v)
        await BugLog.logToBotlog(embed=embed)

@bot.event
async def on_error(event, *args, **kwargs):
    #something went wrong and it might have been in on_command_error, make sure we log to the log file first
    BugLog.error(f"error in {event}\n{args}\n{kwargs}")
    BugLog.error(traceback.format_exc())
    embed = discord.Embed(colour=discord.Colour(0xff0000),
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))

    embed.set_author(name=f"Caught an error in {event}:")

    embed.add_field(name="args", value=str(args))
    embed.add_field(name="kwargs", value=str(kwargs))

    embed.add_field(name="Stacktrace", value=traceback.format_exc())
    #try logging to botlog, wrapped in an try catch as there is no higher lvl catching to prevent taking donwn the bot (and if we ended here it might have even been due to trying to log to botlog
    try:
        await BugLog.logToBotlog(embed=embed)
    except Exception as ex:
        BugLog.exception(f"Failed to log to botlog, either Discord broke or something is seriously wrong!\n{ex}", ex)


@bot.event
async def on_guild_join(guild: discord.Guild):
    BugLog.info(f"A new guild came up: {guild.name} ({guild.id}).")
    Configuration.loadConfig(guild)


@bot.event
async def on_ready():
    if not bot.startup_done:
        await Configuration.onReady(bot)
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}' + f'\nVersion: {discord.__version__}\n')
        await BugLog.onReady(bot)
        await bot.change_presence(activity=discord.Activity(name='event submissions being sent!', type=discord.ActivityType.watching))

bot.run(TOKEN)
