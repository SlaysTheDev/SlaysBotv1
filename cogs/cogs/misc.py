import discord
from discord.ext import commands
import random
import nmap
import ipinfo


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")
            await ctx.message.delete()



    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        """Returns an invite for the bot (not really)"""
        return await ctx.send("**fuck off, you can't invite me to your server.**")
        await ctx.message.delete()



    @commands.command()
    async def uptime(self, ctx):
        """Shows Slaysbotl Bot's uptime"""
        up = abs(self.bot.uptime - int(time.perf_counter()))
        up = str(datetime.timedelta(seconds=up))
        await self.bot.say("`Uptime: {}`".format(up))
        await ctx.message.delete()


    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails','Your Gay']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
        await ctx.message.delete()





def setup(client):
    client.add_cog(Misc(client))