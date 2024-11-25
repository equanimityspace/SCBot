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
        button = Button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩", custom_id="3")
        self.add_item(button)

# Create ticket embed
class FeedbackEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(channel) -> None:
        embed = nextcord.Embed(title="S&C Client Feedback", description="Please fill out the below template, Ryan or Fred will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nCompany (N/A if none):\nPositive Feedback:\nWhat we can improve:", inline=False)
        await channel.send(embed=embed)

class Feedback(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # add command
    @slash_command(name="createfeedbackticket", description="Create an embed and button for a client feedback ticket")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="S&C Client Feedback", description="To provide feedback react with 📩\nThese tickets will only be seen by Ryan Copeland and Fred Snow.", color=16777215)
        
        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)

def setup(bot) -> None:
    bot.add_cog(Feedback(bot))
