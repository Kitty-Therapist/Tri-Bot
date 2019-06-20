import json
import sys
import os
import copy
import traceback
import discord
from discord.ext import commands
from discord import utils
from utils import Util, BugLog, Permission

MASTER_CONFIG = dict()
SERVER_CONFIGS = dict()

CONFIG_TEMPLATE = {
    "GENERAL_ART_CHANNEL": 0,
    "FAN_ART_CHANNEL": 0,
    "EMOJIS_CHANNEL": 0,
    "MERCH_CHANNEL": 0,
    "MUSIC_CHANNEL": 0,
    "STORY_CHANNEL": 0, 
    "GENERAL_BOT_CHANNEL": 0,
    "FUNCTIONAL": 0,
    "ENTERTAINMENT": 0,
    "SHITPOST": 0,
    "CENSORED_LOGS": 0
}

async def onReady(bot:commands.Bot):
    BugLog.info(f"Loading configurations for {len(bot.guilds)} guilds")
    for guild in bot.guilds:
        BugLog.info(f"Loading info for {guild.name} ({guild.id})")
        loadConfig(guild)


def loadGlobalConfig():
    global MASTER_CONFIG
    try:
        with open('config/master.json', 'r') as jsonfile:
            MASTER_CONFIG = json.load(jsonfile)
    except FileNotFoundError:
        BugLog.error("Unable to load config, running with defaults.")
    except Exception as e:
        BugLog.error("Failed to parse configuration.")
        print(e)
        raise e


def loadConfig(guild:discord.Guild):
    global SERVER_CONFIGS
    try:
        with open(f'config/{guild.id}.json', 'r') as jsonfile:
            config = json.load(jsonfile)
            for key in CONFIG_TEMPLATE:
                if key not in config:
                    config[key] = CONFIG_TEMPLATE[key]
            SERVER_CONFIGS[guild.id] = config
    except FileNotFoundError:
        BugLog.info(f"No config available for {guild.name} ({guild.id}), creating blank one.")
        SERVER_CONFIGS[guild.id] = copy.deepcopy(CONFIG_TEMPLATE)
        saveConfig(guild.id)

def loadConfigFile(id):
    global SERVER_CONFIGS
    try:
        with open(f'config/{id}.json', 'r') as jsonfile:
            config = json.load(jsonfile)
            for key in CONFIG_TEMPLATE:
                if key not in config:
                    config[key] = CONFIG_TEMPLATE[key]
            SERVER_CONFIGS[id] = config
    except FileNotFoundError:
        BugLog.info(f"No config available for ({guild.id}), creating blank one.")
        SERVER_CONFIGS[id] = copy.deepcopy(CONFIG_TEMPLATE)
        saveConfig(id)

def getConfigVar(id, key):
    if id not in SERVER_CONFIGS.keys():
        loadConfigFile(id)
    return SERVER_CONFIGS[id][key]

def getConfigVarChannel(id, key, bot:commands.Bot):
    return bot.get_channel(getConfigVar(id, key))

def setConfigVar(id, key, value):
    SERVER_CONFIGS[id][key] = value
    saveConfig(id)

def saveConfig(id):
    global SERVER_CONFIGS
    with open(f'config/{id}.json', 'w') as jsonfile:
        jsonfile.write((json.dumps(SERVER_CONFIGS[id], indent=4, skipkeys=True, sort_keys=True)))

def getMasterConfigVar(key, default=None) :
    global MASTER_CONFIG
    if not key in MASTER_CONFIG.keys():
        MASTER_CONFIG[key] = default
        saveMasterConfig()
    return MASTER_CONFIG[key]


def saveMasterConfig():
    global MASTER_CONFIG
    with open('config/master.json', 'w') as jsonfile:
        jsonfile.write((json.dumps(MASTER_CONFIG, indent=4, skipkeys=True, sort_keys=True)))
