import discord
from discord.ext import commands



class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.group(name='help', invoke_without_command=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:

            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name="Base Help Commands")
            embed.add_field(name=":tada: Fun", value='``.help fun``- See all fun related commnands', inline=False)
            embed.add_field(name=':tools: Moderation', value='``.help moderation`` -See all utilities and moderation commands', inline=False)
            embed.add_field(name=':notebook: info',value='``.help info`` - See all information related commands', inline=False)
            embed.add_field(name=':ticket: Tickets',value='``.help tickets`` - See all support ticket related commands',inline=False)
            embed.add_field(name=':white_check_mark: Verification',value='``.help verification`` - See all verification related commands',inline=False)




            await ctx.send(embed=embed)



    @help.command(name='fun',)
    async def fun_subcommand(self, ctx):
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

            embed.set_author(name="Fun Commands")
            embed.add_field(name=":slot_machine: Slots", value='``.slots``-Play a Fun Slots Game', inline=False)
            embed.add_field(name='Invite',value='``.invite`` - Invite this bot to your discord', inline=False)
            




            await ctx.send(embed=embed)



    @help.command(name='moderation',)
    async def moderation_subcommand(self, ctx):
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
            
            embed.set_author(name="Moderation Commands")
            embed.add_field(name='Kick', value='``.kick [user]`` - Kicks a user from the discord server',inline=False)
            embed.add_field(name='Ban', value='``.ban [user]`` - Bans a user from the discord server',inline=False)
            embed.add_field(name='Banifno', value='``.baninfo [user id]`` - Retrives a reason why a user was banned from audit log',inline=False)
            embed.add_field(name='Mute', value='``.mute [user]`` - mutes a user from the discord server',inline=False)
            embed.add_field(name='Warn', value='``.warn [user]`` - Warn a user for being naughty',inline=False)
            embed.add_field(name='Clear', value='``.clear [amount]`` - Purges a specified amount of messages',inline=False)

            await ctx.send(embed=embed)


    @help.command(name='info',)
    async def info_subcommand(self, ctx):
            embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
            
            embed.set_author(name="Info Commands")
            embed.add_field(name='ServerInfo', value='``.sinfo`` - See information about the server',inline=False)
            embed.add_field(name='UserInfo', value='``.uinfo [user]`` - See information about the giver user',inline=False)
            embed.add_field(name='ServerInfo', value='``.sinfo`` - See information about the server',inline=False)
            embed.add_field(name='About', value='``.about`` - See info about the developer and the bot', inline=False)
            embed.add_field(name='VPN Prices', value='``.prices`` - See the current prices of the VPNst', inline=False)
            embed.add_field(name='Net Prices', value='``.nets`` - See the current prices for Botnet spots', inline=False)
            embed.add_field(name='Status', value='``.status`` - See current status of VPN servers (auto updates)', inline=False)

            await ctx.send(embed=embed)


    @help.command(name='tickets',)
    async def tickets_subcommand(self, ctx):
        await ctx.send('**this is a WiP**')




    @help.command(name='verification',)
    async def verification_subcommand(self, ctx):
        await ctx.send('**This is a WiP**')


def setup(client):
    client.add_cog(Help(client))