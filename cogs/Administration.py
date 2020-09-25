import discord as dc
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        brief='Do something to a member',
        description='Do something to a member, like kick or ban them.'
    )
    async def mem(self, ctx):  # self, ctx, otherArg, anotherArg, etc.
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid user command.')

    @has_permissions(kick_members)
    @mem.command(
        name='kick',
        brief='Kicks a member.',
        description='Kick a member, optionally specifying a reason.'
    )
    async def kick(self, ctx, mention: dc.Member, *, reason: str = None):  # self, ctx, otherArg, anotherArg, etc.
        await mention.kick(reason=f'By {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}): {reason}')
        await ctx.send(f'Kicked {mention.name}#{mention.discriminator} ({mention.id}) for: ```{reason}```')

    @has_permissions(ban_members)
    @mem.command(
        brief='Ban a member.',
        description='Ban a member, optionally specifying a reason.'
    )
    async def ban(self, ctx, mention: dc.Member, *, reason: str = None):  # self, ctx, otherArg, anotherArg, etc.
        await mention.ban(reason=f'By {ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}): {reason}')
        await ctx.send(f'Banned {mention.name}#{mention.discriminator} ({mention.id}) for: ```{reason}```')


def setup(bot):
    bot.add_cog(Admin(bot))
