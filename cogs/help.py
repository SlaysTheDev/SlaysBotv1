import discord
from discord.ext import commands



class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self,ctx,):
        

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="Help Commands" ,icon_url=ctx.author.avatar_url)

        embed.add_field(name='``Ping``' , value="Responds with your ping to the bot")
        embed.add_field(name='``Serverinfo``', value="**Show's information about the server**",)
        embed.add_field(name='``Slots``' , value="Fun Slots Game",)
        embed.add_field(name='``botinfo``', value="**Show's information about the Developer**",)
        embed.add_field(name='``Info``', value="**Show's information about a user**", )
        embed.add_field(name='```Ban```', value="**Bans a user from the discord** (__Requires Ban Permissions__)", )
        embed.add_field(name='``Kick``', value="**Kicks a user from the discord** (__Requires Kick Permissions__)", )
        embed.add_field(name='``Mute``', value="**Mutes a user for a given duration** (__Requires Mute Permissions__)",)
        embed.add_field(name='``UnMute``', value="**Unmutes a muted user** (__Requires UnMute Permissions__)",)
        embed.add_field(name='``Baninfo``', value="**Show's a reason why a user was banned** (__Requires Audit log Permissions__)",)
        embed.add_field(name='``Clear``', value="**Purges a specified amount of messages** (__Requires Manage messages Permissions__)")
        embed.add_field(name='``Warn``', value="**Warn's a user**")
        embed.add_field(name='``Invite``', value="**Invite this bot to your discord**")
        embed.add_field(name='``Whois``', value="**Domain to IPs**")
        embed.add_field(name='``ServerStatus``',value="**Displays the current status of the VPN servers**")
        embed.add_field(name='```HowtoBuy```',value='**Shows a guide on how to buy**')
        
        await ctx.message.author.send(embed=embed)
        await ctx.send(f'``Commands have been sent to you in a dm``')





        


def setup(client):
    client.add_cog(Help(client))