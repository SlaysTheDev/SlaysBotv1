import discord
from discord.ext import commands

class Buy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['howtobuy'])
    async def buy(self, ctx,):

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="How to buy VPNs/Stresser Plans", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Buying a VPNs", value="To buy a VPN send the amount of the desired plan to my BTC or Cashapp address then message me on discord", inline=True)
        embed.add_field(name="Buying Stresser Plans", value="Not currently available **Comming SOON**", inline=True)
        embed.add_field(name="Cash App payments", value="$SlaysVPNs, When sending payment via cash app please add the note **For VPN** or **For Stresser** also make sure you add your discord tag", inline=True)
        embed.add_field(name="BTC Payments", value="3Dg7xS3WKB8X6vtihQT7VsHZ1Aj7TdE1xs, All BTC payments __ARE NON REFUNDABLE__ **MESSAGE ME AFTER SENDING**",inline=True)
        embed.add_field(name="Please Note", value="Please remember that i have a life to so be patient if i don't respond isntantly ",inline=True)


        await ctx.message.author.send(embed=embed)
        await ctx.send('**Check your DMs**')
        await ctx.message.delete()




    @commands.command(aliases=['serverstatus'])
    async def status(self, ctx):

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="VPN Status",)
        embed.add_field(name=':flag_de: ``Link 11 + Corero Server``', value="Status Online :white_check_mark: ",inline=True)
        embed.add_field(name=':flag_ca: ``OVH Server 1``', value="Status Online :white_check_mark: ",inline=False)
        embed.add_field(name=':flag_ca: ``OVH Server 2``', value="Status Offline :x: ",inline=False)
        embed.add_field(name=":flag_us: ``Path Server``", value="Status Online :white_check_mark:",inline=True)
        embed.set_footer(text='Automaticaly updates')



        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command(aliases=['price'])
    async def prices(self, ctx):

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name="VPN Prices",)
        embed.add_field(name='**1 Month VPN Package**', value='``$5``',inline=True)
        embed.add_field(name='**3 Months VPN Package**', value='``$15``',inline=False)
        embed.add_field(name='**1 Year VPN Package (3 Concurrent connections)**', value="``$60``",inline=True)
        embed.add_field(name='**Extra Concurrents**', value="Extra Concurrents are ``$2`` per concurrent connection")


        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(aliases=['nets','net prices'])
    async def netprice(self, ctx):

        embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.add_field(name='1 Month Spot', value='$10',inline=True)
        embed.add_field(name='``3`` Months Spot', value='$30',inline=True)
        embed.add_field(name='``1`` Year Spot', value='$60',inline=True)
        embed.add_field(name='To Purchase a Spot Contact ', value='**AssaSSAins301#6401**')
        


        await ctx.send(embed=embed)
        await ctx.message.delete()




def setup(client):
    client.add_cog(Buy(client))