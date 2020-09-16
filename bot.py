# Import essentials:
import os
import asyncio
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands
from datetime import datetime

# Important Stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(
    command_prefix='-',
    allowed_mentions=discord.AllowedMentions(
        everyone=False,
        users=True,
        roles=False),
    owner_id=386731759729115137
)
config_channel = 752723937942831143
cogList = []
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
        cogList.append(f'{file[:-3]}')


def now():
    return str(datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
# Thanks <@302956027656011776> (Ernest Izdebski) for the above code.


@bot.event
async def on_ready():
    print(f'Day and Time: {now()}')
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game('my role as a robot')
    await bot.change_presence(activity=game)
    # Send "online" message
    channel = bot.get_channel(config_channel)
    await channel.send(':green_circle: Online!')
    # See: https://discordpy.readthedocs.io/en/latest/api.html#activity


@bot.command(name='filler', brief='A filler, does nothing.')
async def filler(ctx):
    pass


@bot.command()
async def showcogs(ctx):
    await ctx.send(f"{', '.join(cogList)}")


@bot.command()
async def embedcreate(ctx):
    def check(message):
        return ctx.message.author == ctx.author and message.guild.id == ctx.guild.id
    await ctx.send(embed=discord.Embed(
        description="Input title")
    )
    title = await bot.wait_for('message', check=check, timeout=180.0)
    await ctx.send(embed=discord.Embed(
        description='Input description.')
    )
    description = await bot.wait_for('message', check=check, timeout=None)
    await ctx.send(embed=discord.Embed(
        description="Let's roll! I'm generating your final embed now! Please wait.."),
        delete_after=3)
    embed = discord.Embed(
        title=title.content,
        description=description.content
    )
    await ctx.send(embed=embed)


@bot.command()
async def embedcreate2(ctx):
    def check(message):
        return ctx.message.author == ctx.author and message.guild.id == ctx.guild.id
    author = ctx.message.author
    generate = await ctx.send(embed=discord.Embed(
        description="Input title"))
    title = await bot.wait_for(
        'message',
        check=check,
        timeout=180.0
    )
    await generate.edit(embed=discord.Embed(
        description="Input description"))
    description = await bot.wait_for('message', check=check, timeout=180.0)

    await generate.edit(embed=discord.Embed(
        description="Let's roll! I'm generating your final embed now! Please wait.."),
        delete_after=5)
    embed = discord.Embed(
        title=title.content,
        description=description.content
    )
    await ctx.send(embed=embed)


@bot.command()
async def edit(ctx):
    message = await ctx.send('testing')
    await asyncio.sleep(0.3)
    await message.edit(content='v2')


bot.run(TOKEN)
