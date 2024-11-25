import nextcord
from nextcord import Interaction, slash_command
from nextcord.ui import Button, View
from nextcord.ext import commands
from nextcord.ext.commands import Bot, Cog

# Create Button
class TicketButton(View):
    def __init__(self) -> None:
        super().__init__()

        # create button
        button = Button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩", custom_id="0")
        self.add_item(button)

# Create ticket embed
class AttorneyEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(channel) -> None:
        embed = nextcord.Embed(title="Attorney Request Ticket", description="Please fill out the below template, an S&C Attorney will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nCompany (N/A if none):\nEvidence (N/A if none):\nDetailed description of request:", inline=False)
        await channel.send(embed=embed)

class AttorneyRequest(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # add command
    @slash_command(name="createattorneyrequest", description="Create an embed and button for an attorney request ticket")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="Attorney Request Ticket", description="To create an attorney request ticket react with 📩\n\nUsed for anyone who would like to hire Snow & Copeland P.C. and does not have an existing contract agreement.", color=16777215)
        
        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)

def setup(bot) -> None:
    bot.add_cog(AttorneyRequest(bot))
