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
        button = Button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩", custom_id="4")
        self.add_item(button)

# Create ticket embed
class TicketEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(channel) -> None:
        embed = nextcord.Embed(title="Role Request Ticket", description="Please fill out the below template, an S&C Attorney will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nRole:\nProof (roster, etc):", inline=False)
        await channel.send(embed=embed)

class RoleRequest(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # add command
    @slash_command(name="createrolerequest", description="Create an embed and button for a role request ticket")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="Role Request Ticket", description="To request a role (bar certified, judge, etc) react with 📩", color=16777215)
        
        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)

def setup(bot) -> None:
    bot.add_cog(RoleRequest(bot))