# This module is useful for getting general information
# on things lke users and the guild the bot is in.

import discord
from discord.ext import commands
import random

dc = discord


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='accinfo',
        aliases=['account', 'user'],
        brief='Diplays basic user account information',
        description='''
        Displays user information
        '''
    )
    async def account_information(self, ctx, mention: dc.Member = None):
        if mention is None:
            mention = ctx.message.author
        # For statuses (smh, I hope I can optimise this.)
        desk, mobile, web = None, None, None
        disOn = dc.Status.online
        disId = dc.Status.idle
        disDn = dc.Status.dnd
        disOf = dc.Status.offline
        if mention.desktop_status == disOn:
            desk = ':green_circle:'
        elif mention.desktop_status == disId:
            desk = ':yellow_circle'
        elif mention.desktop_status == disDn:
            desk = ':red_circle:'
        elif mention.desktop_status == disOf:
            desk = ':white_circle:'
        if mention.mobile_status == disOn:
            mobile = ':green_circle:'
        elif mention.mobile_status == disId:
            mobile = ':yellow_circle'
        elif mention.mobile_status == disDn:
            mobile = ':red_circle:'
        elif mention.mobile_status == disOf:
            mobile = ':white_circle:'
        if mention.web_status == disOn:
            web = ':green_circle:'
        elif mention.web_status == disId:
            web = ':yellow_circle'
        elif mention.web_status == disDn:
            web = ':red_circle:'
        elif mention.web_status == disOf:
            web = ':white_circle:'

        embedUserInfo = dc.Embed(title=f'{mention.name}#{mention.discriminator}', colour=mention.colour)
        embedUserInfo.set_thumbnail(url=mention.avatar_url)
        embedUserInfo.add_field(name='Display Name', value=mention.display_name, inline=True)
        embedUserInfo.add_field(name='ID', value=mention.id, inline=True)
        embedUserInfo.add_field(name='Created at (UTC)', value=mention.created_at, inline=False)
        embedUserInfo.add_field(name='Joined guild at (UTC)', value=mention.joined_at, inline=False)
        embedUserInfo.add_field(name='Status', value=f'{desk} Desktop: **{mention.desktop_status}**\n{mobile} Mobile: **{mention.mobile_status}**\n{web} Browser: **{mention.web_status}**', inline=False)
        await ctx.send(embed=embedUserInfo)

    @commands.command(
        name='serverinfo', aliases=['server,'],
        brief='Displays basic server information',
        description='''
        Displays server name, server icon, server ID, server region, no. of channels and no. of members
        ''')
    async def server_information(self, ctx):
        # Counting Members, thanks StackOverFlow. Honestly I don't understand *why* the below works.
        botCount = len([b for b in ctx.guild.members if b.bot])
        humanCount = len([m for m in ctx.guild.members if not m.bot])

        # Counting Channels. Format taken from above, still don't know how it works. But it works.
        categoryCount = len(
            [cat for cat in ctx.guild.channels if cat.type is dc.ChannelType.category]
        )
        textCount = len(
            [t for t in ctx.guild.channels if t.type is dc.ChannelType.text]
        )
        voiceCount = len(
            [v for v in ctx.guild.channels if v.type is dc.ChannelType.voice]
        )

        # Finally, embeded content.
        embedServerInfo = dc.Embed(
            title=f'{ctx.message.guild.name}',
            colour=discord.Colour.blurple()
        )
        embedServerInfo.set_thumbnail(
            url=ctx.guild.icon_url
        )
        embedServerInfo.add_field(
            name='Owner',
            value=f'{ctx.guild.owner}',
            inline=False
        )
        embedServerInfo.add_field(
            name='Guild ID',
            value=f'{ctx.guild.id}', inline=True)
        embedServerInfo.add_field(
            name='Region',
            value=f'{ctx.guild.region}', inline=True
        )
        embedServerInfo.add_field(
            name='Channels',
            value=f'Categories: {categoryCount}\nText: {textCount}\nVoice: {voiceCount}',
            inline=False
        )
        embedServerInfo.add_field(
            name='Members of Guild',
            value=f'Total: {humanCount + botCount}\nPeople: {humanCount}\nBots: {botCount}',
            inline=False
        )
        await ctx.send(embed=embedServerInfo)


def setup(bot):
    bot.add_cog(Utilities(bot))
