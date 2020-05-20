import discord
from discord.ext import commands



class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self,ctx,):
        

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Help Commands" ,icon_url=ctx.author.avatar_url)

        embed.add_field(name='Ping', value='**Says your ping**', inline=False)
        embed.add_field(name='Serverinfo', value="**Show's information about the server**", inline=False)
        embed.add_field(name='About', value="**Show's information about the Developer**",inline=False)
        embed.add_field(name='Info', value="**Show's information about a user**", inline=False)
        embed.add_field(name='Ban', value="**Bans a user from the discord** (__Requires Ban Permissions__)", inline=False)
        embed.add_field(name='Kick', value="**Kicks a user from the discord** (__Requires Kick Permissions__)", inline=False)
        embed.add_field(name='Mute', value="**Mutes a user for a given duration** (__Requires Mute Permissions__)", inline=False)
        embed.add_field(name='UnMute', value="**Unmutes a muted user** (__Requires UnMute Permissions__)", inline=False)
        embed.add_field(name='Baninfo', value="**Show's a reason why a user was banned** (__Requires Audit log Permissions__)", inline=False)
        embed.add_field(name='Clear', value="*Purges a specified amount of messages** (__Requires Manage messages Permissions__)", inline=False)
        embed.add_field(name='Warn', value="**Warn's a user**", inline=False)

        await ctx.message.author.send(embed=embed)
        


def setup(client):
    client.add_cog(Help(client))