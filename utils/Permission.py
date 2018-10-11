from discord.ext import commands

from utils import Configuration


def is_owner():
    async def predicate(ctx):
        return ctx.bot.is_owner(ctx.author)
    return commands.check(predicate)

def head_only():
    async def predicate(ctx):
        return ctx.author.id in [187606096418963456, 298618155281154058, 169197827002466304, 263495765270200320, 117101067136794628, 164475721173958657, 191793155685744640]
    return commands.check(predicate)


def isServerAdmin(ctx:commands.Context):
    if ctx.guild is None:
        return False
    adminrole = Configuration.getConfigVar(ctx.guild.id, "ADMIN_ROLE_ID")
    if adminrole != 0:
        for role in ctx.author.roles:
            if str(role.id) == str(adminrole):
                return True
    return ctx.author == ctx.guild.owner


def isServerMod(ctx:commands.Context):
    if ctx.guild is None:
        return False
    modrole = Configuration.getConfigVar(ctx.guild.id, "MOD_ROLE_ID")
    if modrole != 0:
        for role in ctx.author.roles:
            if str(role.id) == str(modrole):
                return True
    return isServerAdmin(ctx)
