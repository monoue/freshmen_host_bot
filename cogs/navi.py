from discord.ext import commands
from utils.check_privilege import executed_by_privileged_member
import config
import emoji
import random


def is_exception(USERS_NUM):
    EXCEPTIONS = [1, 2, 5]
    for exc in EXCEPTIONS:
        if USERS_NUM == exc:
            return True
    return False


def get_capacity_per_room(users_num):
    ROOMS_NUM = users_num // 3
    capacity_per_room = [3] * ROOMS_NUM
    REMAINDER = users_num % 3
    for i in range(REMAINDER):
        capacity_per_room[i] += 1
    return capacity_per_room


def make_line(room_num, room_members):
    return f"{room_num}号室: {' / '.join(room_members)}\n"


def get_result_str(users):
    USERS_NUM = len(users)
    if USERS_NUM == 0:
        return False

    if is_exception(USERS_NUM):
        result_str = make_line(1, users)
        return result_str

    CAPACITY_PER_ROOM = get_capacity_per_room(USERS_NUM)
    random.shuffle(users)
    result_str = ''
    start_i = 0
    for i, capacity in enumerate(CAPACITY_PER_ROOM, start=1):
        end_i = start_i + capacity
        result_str += make_line(i, users[start_i:end_i])
        start_i += capacity
    return result_str


class Navi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def navi(self, ctx):
        if not executed_by_privileged_member(ctx):
            return
        channel = self.bot.get_channel(config.CHANNEL_ID)
        msg = await channel.fetch_message(config.MESSAGE_ID)
        reactions = msg.reactions
        users = []
        for reaction in reactions:
            if emoji.demojize(reaction.emoji) == ':thumbs_up:':
                reaction_users = await reaction.users().flatten()
                for user in reaction_users:
                    users.append(user.mention)
                break
        result_str = get_result_str(users)
        await ctx.send(result_str)


def setup(bot):
    bot.add_cog(Navi(bot))
