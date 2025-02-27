# Required libraries:


import discord
from discord.ext import commands
from os import listdir
from typing import Any


# Sensitive variables:


BOT_TOKEN = "" # Insert your bot token here.
BOT_PREFIX = "" # Input your bot's prefix here (e.g., "!", "?", etc.).


# Class "Bot":


class Bot(commands.Bot):
    def __init__(self, intents: discord.Intents, **kwargs: Any):
        super().__init__(
            command_prefix=BOT_PREFIX,
            allowed_mentions=discord.AllowedMentions(roles=True, users=True, everyone=True),
            case_insensitive=True,
            intents=discord.Intents.all()
        )

    async def load_commands(self):
        self.remove_command("help")
        for file in listdir("commands"):
            if file.endswith(".py"):
                await self.load_extension(f"commands.{file[:-3]}")

    async def on_message(self, message: Any):
        if not message.author.bot:
            await self.process_commands(message)

    async def on_command_error(self, ctx: Any, error: Any):
        if isinstance(error, commands.CheckFailure):
            return

    async def on_ready(self):
        await self.load_commands()
        await self.tree.sync()
        print(f"✅・Initialized successfully!")


# Instance for the "Bot" class:


bot = Bot(intents=discord.Intents.all())


# "Bot" instance initialization:


try:
    bot.run(BOT_TOKEN)
except Exception as error:
    print(f"❌・The following error occurred while trying to initialize: \033[1;31m{error}\033[0m")