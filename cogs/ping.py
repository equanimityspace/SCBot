from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @slash_command(name="ping", description="Check bot latency")
    async def ping(self, inter: Interaction) -> None:
        await inter.send(f'Latency is {self.bot.latency * 1000:.2f}ms')

def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))