import discord
from discord.ext import commands
import request 
import json
import os
from discord.ext.commands import bot
import whois
import socket
import re 

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command() #Get the ping of the Discord bot
    async def ping(self, ctx): # This was inside '__init__' before
        await ctx.send(f'> Your Ping is {round(self.client.latency * 1000)}ms :hourglass:')







def setup(client):
    client.add_cog(Ping(client))
