import discord
import os
from discord.ext import commands
import datetime
import asyncio 
import socket
import json
import ipinfo
import requests
import whois
client = commands.Bot(command_prefix ='.',case_insensitive=True) # Sets the prfix of the Bot
client.remove_command('help') #removes help command so you can customize your own
#os.chdir('/root/SlaysBotv1/cogs')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="Type .help for Help"))
    print("Bot is ready.")   




@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome to SlaysVPNs You are the {len(list(member.guild.members))} member",)
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=710956039876378698)

    await channel.send(embed=embed)


@client.command()
async def load(ctx, extension,):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Loaded **{extension}.py**")

@client.command()
async def unload(ctx, extension,):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Unloaded **{extension}.py**")

@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Reloaded **{extension}.py**")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name='Members')
    await member.add_roles(role)













client.run('TOKEN')
