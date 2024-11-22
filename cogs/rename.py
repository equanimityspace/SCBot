import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

class RenameChannel(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @slash_command(name="rename", description="rename the current channel")
    async def rename(self, inter: Interaction, new_name):
        # get current channel name and category that all tickets go in
        channel = inter.channel
        channel_category = inter.channel.category_id
        guild = inter.guild
        ticket_category = 1309294281034301552

        # rename channel if it is in the ticket category
        if channel_category == ticket_category:
            await channel.edit(name=str(new_name))
            await inter.send("Channel renamed successfully", ephemeral=True)
        else:
            await inter.send("This channel is not a ticket")

def setup(bot) -> None:
    bot.add_cog(RenameChannel(bot))
