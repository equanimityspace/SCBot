import nextcord
from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog

# Create Button
class TicketButton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    # create the button
    @nextcord.ui.button(label="Create Ticket", style=nextcord.ButtonStyle.secondary, emoji="📩") 
    # add button functionality
    async def button_callback(self, button: nextcord.ui.Button, inter: Interaction) -> None:
        guild = inter.guild
        category = guild.get_channel(1309294281034301552)
        # permissions
        overwrites = {
            inter.user: nextcord.PermissionOverwrite(read_messages=True),
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False) # TODO figure out how to define a default
        }

        channel = await category.create_text_channel(name=f'{inter.user}-attorney-request', topic="Attorney Request Ticket", position=0, overwrites=overwrites)
        await TicketEmbed.ticket_embed(self, channel)
        await inter.send(f'Ticket created successfully', ephemeral=True)
        self.value = True

# Create ticket embed
class TicketEmbed():
    def __init__(self, channel) -> None:
        super().__init__()
        self.value = None

    print("read TicketEmbed Class") # debug
    # create embed
    async def ticket_embed(self, channel) -> None:
        print("entered def ticket embed") # debug
        embed = nextcord.Embed(title="Attorney Request Ticket", description="Please fill out the below template, an S&C Attorney will be in contact shortly.", color=16777215)
        embed.add_field(name="Template:", value="Name:\nCompany (N/A if none):\nEvidence (N/A if none):\nDetailed description of request:", inline=False)
        await channel.send(embed=embed)
        self.stop()

class AttorneyRequestCreate(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    # add commandE
    @slash_command(name="createattorneyrequest", description="Create an embed and button for an attorney request ticket")
    async def prompt_embed(self, inter: Interaction) -> None:
        embed = nextcord.Embed(title="Attorney Request Ticket", description="To create an attorney request ticket react with 📩\n\nUsed for anyone who would like to hire Snow & Copeland P.C. and does not have an existing contract agreement.", color=16777215)

        # Add button to UI and send message
        view = TicketButton()
        await inter.send(embed=embed, view=view)
        await view.wait()

def setup(bot: Bot) -> None:
    bot.add_cog(AttorneyRequestCreate(bot))