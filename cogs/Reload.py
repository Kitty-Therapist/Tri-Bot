import os
import asyncio 
import subprocess
import configparser
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import traceback
from subprocess import Popen
from discord.ext import commands

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot
        self._last_result = None 

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    @commands.command(hidden=True)
    async def reload(self, ctx, *, cog: str):
        cogs = []
        for c in ctx.bot.cogs:
            cogs.append(c.replace('Cog', ''))

        if cog in cogs:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f'**{cog}** has been reloaded')
        else:
            await ctx.send(f"I can't find that cog.")

    @commands.command(hidden=True)
    async def load(self, ctx, cog: str):
        if os.path.isfile(f"cogs/{cog}.py") or os.path.isfile(f"BrilliantGhoulBot/cogs/{cog}.py"):
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"**{cog}** has been loaded!")
        else:
            await ctx.send(f"I can't find that cog.")

    @commands.command(hidden=True)
    async def unload(self, ctx, cog: str):
        cogs = []
        for c in ctx.bot.cogs:
            cogs.append(c.replace('Cog', ''))
        if cog in cogs:
            self.bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f'**{cog}** has been unloaded')
        else:
            await ctx.send(f"I can't find that cog.")
            
    @commands.command(hidden=True)
    async def restart(self, ctx):
        """Restarts the bot"""
        await ctx.send("Restarting...")
        await self.bot.logout()
        await self.bot.close()

    @commands.command(pass_context=True, hidden=True, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""
        if "token" in body:
            await ctx.send("No token stealing allowed.")
            return

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')


def setup(bot):
    bot.add_cog(Reload(bot))
