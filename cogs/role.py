import discord
from discord.ext import commands
from datetime import datetime
import config
from dateutil.relativedelta import relativedelta


class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def role_exists(self, guild, name) -> bool:
        for role in guild.roles:
            if role.name == name:
                return True
        return False

    async def create_role(self, guild, name, color=None):
        if self.role_exists(guild, name):
            return
        if color is None:
            await guild.create_role(name=name)
        else:
            await guild.create_role(name=name, colour=color)

    @commands.command()
    async def create_freshman_role(self, ctx):
        name = "role_freshman"
        color = 0xf172a3
        await self.create_role(ctx.guild, name, color)

    @commands.command()
    async def create_core_time_role(self, ctx):
        name = "core_time"
        await self.create_role(ctx.guild, name)

    def role_is_already_given(self, role, given_roles):
        return role in given_roles

    def is_student(self, member_roles) -> bool:
        for role in member_roles:
            if role.name == "student":
                return True
        return False

    async def add_role_if_appropriate(self, member, role):
        if self.role_is_already_given(role, member.roles):
            return
        if not self.is_student(member.roles):
            return
        if member.joined_at > datetime.now() - relativedelta(weeks=1):
            await member.add_roles(role)

    async def add_role_entirely(self, ctx, role_name):
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
        role_name = "role_freshman"
        await self.add_role_entirely(ctx, role_name)

def setup(bot):
    bot.add_cog(Role(bot))
