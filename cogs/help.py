import discord
from discord.ext import commands
import config


class Help(commands.Cog):
    @commands.command()
    async def help(self, ctx):
        nick = ctx.author.nick
        name = ctx.author.name if nick is None else nick
        help_msg = f"{name}さん…新入生コアタイム不人気すぎて、助けてほしいのはこっちです"
        await ctx.send(help_msg)


def setup(bot):
    bot.add_cog(Help(bot))
