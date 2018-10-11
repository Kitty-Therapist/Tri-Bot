from discord.ext import commands
from discord import  Role, TextChannel
from utils import Configuration, Permission
from utils.Permission import head_only


class EventSetup:
    def __init__(self, bot):
        pass

    async def __local_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @head_only()
    @commands.guild_only()
    @commands.group(hidden=True)
    async def configure(self, ctx: commands.Context):
        """Configure server specific settings."""
        if ctx.subcommand_passed is None:
            await ctx.send("See the subcommands (+help configure) for configurations.")

    @head_only()
    @configure.command(hidden=True)
    async def submission(self, ctx: commands.Context, channel:TextChannel):
        """Sets the submission channel."""
        Configuration.setConfigVar(ctx.guild.id, "SUBMISSION_CHANNEL", channel.id)
        await ctx.send(f"The submission channel now is {channel.mention}")

    @head_only()
    @configure.command(hidden=True)
    async def modrole(self, ctx: commands.Context, role:Role):
        """Sets the role with moderation rights."""
        Configuration.setConfigVar(ctx.guild.id, "MOD_ROLE_ID", role.id)
        await ctx.send(f"The server moderation role is now `{role.name}`.")

def setup(bot):
    bot.add_cog(EventSetup(bot))
