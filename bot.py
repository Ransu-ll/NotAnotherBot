# Import essentials:
import os
import asyncio
import sys
from dotenv import load_dotenv
import discord
import json
from discord.ext import commands
from datetime import datetime

# Important Stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


# Thanks https://www.youtube.com/watch?v=yrHbGhem6I4&ab_channel=Lucas
def get_prefix(bot, message):
    # Working with dictionaries.
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)

    return prefixes[str(message.guild.id)]


# Initialise bot
bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(
        everyone=False,
        users=True,
        roles=False
    ),
    owner_ids=[386731759729115137]
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


# For custom prefixes per server
@bot.event
async def on_guild_join(guild):
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(guild.id)] = '-'
    # When bot joins server, default prefix will be "-"

    with open('./config/prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)
    # After joining, "dump" server ID as Key and default prefix as Value


@bot.event
async def on_guild_remove(guild):
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes.pop(str(guild.id))
    # When bot leaves server, remove the Key-Value pair.

    with open('./config/prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)
    # After leaving, ensure that the new values (which are blank) are removed from ./config/prefixes.json


@bot.command(
    name='changeprefix'
)
async def change_prefix(ctx, prefix):
    with open('./config/prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(ctx.guild.id)] = prefix
    # If a valid change, set prefix to whatever is specified as the prefix.

    with open('./config/prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent=4)
    # "Dump" new prefix into the dictionary located in ./config/prefixes.json
    await ctx.send(f'The new prefix is now `{prefix}`')


@bot.command()
async def showcogs(ctx):
    await ctx.send(f"{', '.join(cogList)}")

# Required
bot.run(TOKEN)
