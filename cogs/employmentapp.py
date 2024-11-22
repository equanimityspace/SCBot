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
        button = Button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩", custom_id="2")
        self.add_item(button)

# Create ticket embed
class TicketEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(channel) -> None:
        embed = nextcord.Embed(title="S&C Employment Application", description="Please fill out the below template, an S&C Partner will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nBar No.:\n\nFill out the [application form](https://docs.google.com/forms/d/1VjZ42btm6BgcTboGmoQ5SWB3n2fRgwpVxJZw8nu4R8I/edit), and notify a partner when you have completed it.", inline=False)
        await channel.send(embed=embed)

class EmploymentRequest(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    # add command
    @slash_command(name="createemploymentrequest", description="Create an embed and button for an employment application")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="S&C Employment Application", description="To submit an employment application react with 📩", color=16777215)
        
        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)

def setup(bot) -> None:
    bot.add_cog(EmploymentRequest(bot))