# Required libraries:


from discord.ext import commands
from typing import Any
from random import choice


# List of available curiosities:


curiosities = [
    "🐍・Python's scientific name is *Pythonidae*, but in programming, it's just Python.",
    "🐛・The first 'bug' was a real insect: a moth stuck in a computer in 1947.",
    "☕・JavaScript has nothing to do with Java; it was a marketing tactic."
]


# Command used to send a random curiosity:


class Curiosity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="curiosity", description="🧠・Command used to send a random curiosity.")
    async def curiosity(self, ctx: commands.Context[Any]):

        await ctx.defer()
        await ctx.send(content=f"{choice(curiosities)}", reference=ctx.message)


# Method responsible for adding the "Curiosity" command to the "Bot":


async def setup(bot: commands.Bot):
    await bot.add_cog(Curiosity(bot))
