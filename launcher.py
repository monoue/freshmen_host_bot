from discord.ext import commands
import discord
import config


def create_intents() -> discord.Intents:
    intents = discord.Intents().all()
    return intents


class FreshmenHostBot(commands.Bot):
    async def on_ready(self):
        self.load_extension("cogs.change_bot_nickname")
        self.load_extension("cogs.call")
        self.load_extension("cogs.role")
        self.load_extension("cogs.help")
        self.load_extension("cogs.navi")
        print("on_ready")


def main():
    intents = create_intents()
    bot = FreshmenHostBot(command_prefix="!", intents=intents, help_command=None)
    bot.run(config.TOKEN)


if __name__ == "__main__":
    main()
