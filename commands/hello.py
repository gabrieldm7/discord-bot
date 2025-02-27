# Required libraries:


from discord.ext import commands
from typing import Any


# Command used to send a greeting:


class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="hello", description="👋・Command used to send a greeting.", aliases=["hi"])
    async def hello(self, ctx: Any):

        await ctx.defer()
        await ctx.send(content=f"👋・Hello {ctx.author.mention}, how are you?", reference=ctx.message)


# Method responsible for adding the "Hello" command to the "Bot":


async def setup(bot: commands.Bot):
    await bot.add_cog(Hello(bot))