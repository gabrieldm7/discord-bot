# Required libraries:


from discord.ext import commands
from typing import Any
from random import randint


# Command used to roll the dice:


class Roll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="roll", description="🎲・Command used to roll the dice.")
    async def roll(self, ctx: Any, faces: int = 6):

        await ctx.defer()

        if faces <= 0:

            await ctx.send(content=f"❌・The number of faces must be greater than 0.", reference=ctx.message)

        else:

            result = randint(1, faces)
            await ctx.send(content=f"🎲・Result: `{result}`", reference=ctx.message)


# Method responsible for adding the "Roll" command to the "Bot":


async def setup(bot: commands.Bot):
    await bot.add_cog(Roll(bot))