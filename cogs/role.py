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
    
    async def create_role(self, guild, name, color=None):
        if self.role_exists(guild, name):
            return
        if color == None:
            await guild.create_role(name=name)
        else:
            await guild.create_role(name=name, colour=color)
    
    @commands.command()
    async def create_freshman_role(self, ctx):
        name = "freshman"
        color = 0xf172a3
        await self.create_role(ctx.guild, name, color)
    
    @commands.command()
    async def create_core_time_role(self, ctx):
        name = "core_time"
        await self.create_role(ctx.guild, name)
    
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
    
    def is_student(self, member_roles):
        for role in member_roles:
            if role.name == "student":
                return True
        return False

    async def add_role_if_appropriate(self, member, role):
        if self.role_is_already_given(role, member.roles):
            return
        if not self.is_student(member.roles):
            return
        if member.joined_at > datetime.now() - relativedelta(months=1):
            await member.add_roles(role)

    async def add_role_entirely(self, ctx, role_name):
        if not self.executed_by_priviledged_member(ctx):
            return
        guild = ctx.guild
        members = guild.members
        role = discord.utils.get(guild.roles, name=role_name)
        for member in members:
            await self.add_role_if_appropriate(member, role)

    @commands.command()
    async def add_core_time_role_entirely(self, ctx):
        role_name = "core_time"
        await self.add_role_entirely(ctx, role_name)

    @commands.command()
    async def add_freshman_role_entirely(self, ctx):
        role_name = "freshman"
        await self.add_role_entirely(ctx, role_name)
    
    # 全体用の remove も作っておく


def setup(bot):
    bot.add_cog(Role(bot))
