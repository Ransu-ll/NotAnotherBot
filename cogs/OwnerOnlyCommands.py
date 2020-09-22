# This is meant for commands the owner of the bot.
# Things that directly relate to the functionality of the bot,
# like (un/re)loading cogs.

import discord as dc
from discord.ext import commands
from datetime import datetime


def now():
    return str(datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
# Thanks <@302956027656011776> (Ernest Izdebski) for the above code.


class OwnerOnlyCommands(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.group()
    async def cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid cogs command.')

    @cog.command(
        aliases=['restart'],
        brief='Reloads a cog.'
    )
    async def reload(self, ctx, nameOfCog: str):
        try:
            self.bot.reload_extension(f"cogs.{nameOfCog}")
            print(f'At {now()}: {nameOfCog} reloaded')
            await ctx.send(f'{nameOfCog} reloaded!')
        except commands.ExtensionNotLoaded:
            await ctx.send('Cog not loaded.')
        except commands.ExtensionNotFound:
            await ctx.send('Cog not found.')

    @cog.command(
        brief='Unloads a cog.'
    )
    async def unload(self, ctx, nameOfCog):
        try:
            self.bot.unload_extension(f"cogs.{nameOfCog}")
            print(f'At {now()}: {nameOfCog} unloaded')
            await ctx.send(f'{nameOfCog} unloaded!')
        except commands.ExtensionNotLoaded:
            await ctx.send('Cog not loaded.')
        except commands.ExtensionNotFound:
            await ctx.send('Cog not found.')

    @cog.command(
        brief='Loads a cog.'
    )
    async def load(self, ctx, nameOfCog):
        try:
            self.bot.load_extension(f"cogs.{nameOfCog}")
            print(f'At {now()}: {nameOfCog} loaded')
            await ctx.send(f'{nameOfCog} loaded!')
        except commands.ExtensionNotFound:
            await ctx.send('Cog not found.')
        except commands.ExtensionAlreadyLoaded:
            await ctx.send('Cog already loaded.')

    @commands.command(
        brief='[WIP] Stops bot from running.'
    )
    @commands.is_owner()
    async def killbot(self, ctx):
        pass

    @commands.command(
        brief='[WIP] Reloads the bot'
    )
    @commands.is_owner()
    async def reloadbot(self, ctx):
        pass


def setup(bot):
    bot.add_cog(OwnerOnlyCommands(bot))
