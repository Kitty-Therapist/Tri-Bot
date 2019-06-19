import datetime
import logging
import sys
import traceback
import time

import discord
from discord.ext import commands

from utils import Configuration

logger = logging.getLogger('TriBot')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='TriBot.log', encoding='utf-8', mode='w+')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

BOT_LOG_CHANNEL:discord.TextChannel

startupErrors = []


def info(message):
    logger.info(message)


def warn(message):
    logger.warning(message)


def error(message):
    logger.error(message)

def exception(message, error):
    logger.error(message)
    logger.error(traceback.format_tb(error.__traceback__))


# for errors during startup before the bot fully loaded and can't log to botlog yet
def startupError(message, error):
    logger.exception(message)
    startupErrors.append({
        "message": message,
        "exception": error,
        "stacktrace": traceback.format_exc().splitlines()
    }
    


async def onReady(client:commands.Bot):
    global BOT_LOG_CHANNEL
    BOT_LOG_CHANNEL = client.get_channel(591012622745468958)
    if BOT_LOG_CHANNEL is None:
        logger.error("Logging channel is misconfigured, aborting startup!")
        await client.logout()
    info = await client.application_info()
    if len(startupErrors) > 0:
        await logToBotlog(f":rotating_light: Caught {len(startupErrors)} {'exceptions' if len(startupErrors) > 1 else 'exception'} during startup.")
        for error in startupErrors:
            embed = discord.Embed(colour=discord.Colour(0xff0000),
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()))

            embed.set_author(name=error["message"])

            embed.add_field(name="Exception", value=error["exception"])
            stacktrace = ""
            while len(error["stacktrace"]) > 0:
                partial = error["stacktrace"].pop(0)
                if len(stacktrace) + len(partial) > 1024:
                    embed.add_field(name="Stacktrace", value=stacktrace)
                    stacktrace = ""
                stacktrace = f"{stacktrace}\n{partial}"
            if len(stacktrace) > 0:
                embed.add_field(name="Stacktrace", value=stacktrace)
            await logToBotlog(embed=embed)
    await logToBotlog(message=f"{info.name} ready to take off!")


async def logToBotlog(message = None, embed = None, log = True):
    await BOT_LOG_CHANNEL.send(content=message, embed=embed)
    if log:
        info(message)
