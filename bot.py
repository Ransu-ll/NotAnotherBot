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

# Initialise bot
bot = commands.Bot(
    command_prefix='-',
    allowed_mentions=discord.AllowedMentions(
        everyone=False,
        users=True,
        roles=False
    ),
    owner_id=386731759729115137
)
config_channel = 752723937942831143

# Load cogs
cogList = []
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
        cogList.append(f'{file[:-3]}')


# Stuff that may help cut down on code in the future:
def now():
    return str(datetime.today().strftime("%d-%m-%Y %H:%M:%S"))
# Thanks <@302956027656011776> (Ernest Izdebski) for the above code.


# Some very general bot stuff.
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


@bot.command()
async def showcogs(ctx):
    await ctx.send(f"{', '.join(cogList)}")

# Required
bot.run(TOKEN)
