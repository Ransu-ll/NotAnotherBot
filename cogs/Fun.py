# This is for the more "fun" commands for this bot.

import discord as dc
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong')

    @commands.command(
        brief='Bot says whatever follows the command',
        description='Bot says whatever follows the command.')
    async def echo(self, ctx, *, message: str):
        await ctx.send(message)

    @commands.command(brief='Greets the user', description='Greets the user')
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.message.author.mention}!')

    @commands.command(brief='Rolls a die/dice', description='[min] [max] [number of dice]')
    async def rolldice(self, ctx, minimum=1, maximum=6, times=1):
        maxtimes = 15
        if minimum >= maximum:
            await ctx.send('The minimum is greater than the maximum.')
            return
        elif times < 1:
            await ctx.send('You cannot request less than 1 roll!')
            return
        elif times > maxtimes:
            times = maxtimes
            await ctx.send(f'You have requested more than {maxtimes} rolls at once!\nRolls capped.')

        listofdice = []
        for x in range(0, times):
            listofdice.append(str(random.randrange(minimum, maximum + 1)))
        await ctx.send('\n'.join(listofdice))

    @commands.command(name='8ball', brief='Ask 8ball a question', description='Ask 8ball a question. Must include a question mark (?) at the end!')
    async def _8ball(self, ctx, *, message):
        possibleAnswers = (
            'It is certain.', 'It is decidedly so.', 'Without a doubt.',
            'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
            'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
            'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
            'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.",
            'My reply is no.', 'My sources say no.', 'Outlook not so good.',
            'Very doubtful.')

        if message[-1] != '?':
            await ctx.send('Not a question.')
        else:
            await ctx.send(possibleAnswers[random.randrange(0, 20)])


def setup(bot):
    bot.add_cog(Fun(bot))
