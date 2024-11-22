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
        button = Button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩", custom_id="1")
        self.add_item(button)

# Create ticket embed
class TicketEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(channel) -> None:
        embed = nextcord.Embed(title="S&C Client Ticket", description="Please fill out the below template, an S&C Attorney will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nCompany (N/A if none):\nEvidence (N/A if none):\nDetailed description of request:", inline=False)
        await channel.send(embed=embed)

class ClientTicket(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # add command
    @slash_command(name="createclientrequest", description="Create an embed and button for a client request ticket")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="Existing S&C Client Ticket", description="To create an existing client ticket react with 📩\nUsed for any client of Snow & Copeland P.C. with an active contract agreement.", color=16777215)
        
        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)

def setup(bot) -> None:
    bot.add_cog(ClientTicket(bot))
