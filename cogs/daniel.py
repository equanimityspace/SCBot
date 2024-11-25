import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class DanielCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="stimulate", description="trying to stimulate the evidence")
    async def Daniel(self, inter: Interaction):
        await inter.send(content="https://imgur.com/a/j0jNnXG")

def setup(bot) -> None:
    bot.add_cog(DanielCommand(bot))