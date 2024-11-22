import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class NatCommand(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="nat", description="Your Honor...")
    async def Nat(self, inter: Interaction):
        await inter.send(content="https://tenor.com/view/hate-crime-love-crime-hate-crime-saul-gif-25746020")

def setup(bot) -> None:
    bot.add_cog(NatCommand(bot))