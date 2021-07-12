import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import config
import locale

locale.setlocale(locale.LC_ALL, '')


class Call(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = self.init_embed()
        self.caller.start()

    def init_embed(self):
        embed = discord.Embed()
        embed.color = discord.Color.green()
        return embed

    def cog_unload(self):
        self.caller.cancel()

    def make_text(self, now):
        month = now.month
        day = now.day
        weekday = now.strftime('%a')
        return f"{month}/{day}({weekday})開催分です。"\
            "スタンプはお早めに！\n\n"\
            "**新入生コアタイムだよ！ 全員集合！**"

    def is_scheduled_time(self, now):
        hour = 5
        minute = 42
        return now.hour == hour and now.minute == minute
        # FOR TESTING ###
        # return now.second % 5 == 0

    def get_channel(self):
        return self.bot.get_channel(config.CHANNEL_ID)

    # FOR TESTING ###
    # @tasks.loop(seconds=1.0)
    @tasks.loop(minutes=1.0)
    async def caller(self):
        now = datetime.now()
        if self.is_scheduled_time(now):
            await self.bot.wait_until_ready()
            channel = self.get_channel()
            self.embed.description = self.make_text(now)
            msg = await channel.send(embed=self.embed)
            await msg.add_reaction('\N{THUMBS UP SIGN}')

    @commands.command()
    async def call_manually(self, ctx):
        now = datetime.now()
        await self.bot.wait_until_ready()
        self.embed.description = self.make_text(now)
        msg = await ctx.send(embed=self.embed)
        await msg.add_reaction('\N{THUMBS UP SIGN}')


def setup(bot):
    bot.add_cog(Call(bot))
