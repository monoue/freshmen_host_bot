import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import config
from dateutil.relativedelta import relativedelta


class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def role_exists(self, guild, name):
        for role in guild.roles:
            if role.name == name:
                return True
        return False
    
    def create_role(self, guild, name, color=None):
        if self.role_exists(guild, name):
            return
        if color == None:
            guild.create_role(name=name)
        else:
            guild.create_role(name=name, colour=color)
    

    @commands.command()
    async def create_freshman_role(self, ctx):
        name = "freshman"
        color = 0xf172a3
        create_role(ctx.guild, name, color)
    
    @commands.command()
    async def create_core_time_role(self, ctx):
        name = "core_time"
        create_role(ctx.guild, name)
    

    def executed_by_monoue(self, author_id):
        return author_id == config.MONOUE_ID

    def executed_by_staff(author_roles):
        for role in author_roles:
            if role.name == "staff":
                return True
        return False
    
    def executed_by_priviledged_member(self, ctx):
        author = ctx.author
        return self.executed_by_monoue(author.id) or self.executed_by_staff(author.roles)

    def role_is_already_given(self, role, given_roles):
        return role in given_roles
    
    async def add_freshman_role_if_appropriate(self, member, freshman_role):
        if self.role_is_already_given(freshman_role, member.roles):
            return
        if member.joined_at > datetime.now() - relativedelta(months=1)
            await member.add_roles(freshman_role)


    @commands.command()
    async def add_freshman_role_entirely(self, ctx):
        if not self.executed_by_priviledged_member(ctx):
            return
        guild = ctx.guild
        members = guild.members
        freshman_role = discord.utils.get(guild.roles, name="freshman")
        for member in members:
            await self.add_freshman_role_if_appropriate(member, freshman_role)
    
    # 全体用の remove も作っておく


def setup(bot):
    bot.add_cog(Role(bot))
