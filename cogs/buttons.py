import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from cogs.attorneyrequest import TicketEmbed

# Ticket Request Ticket Button Callback
class TicketRequestButton(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_interaction(self, inter: Interaction) -> None:
        guild = inter.guild
        category = guild.get_channel(1309294281034301552)
        
        # permissions
        overwrites = {
            inter.user: nextcord.PermissionOverwrite(read_messages=True),
            guild.default_role: nextcord.PermissionOverwrite(read_messages=False), # Denies access for @everyone, will change to citizen role for S&C server
            guild.get_role(1309298500344746068): nextcord.PermissionOverwrite(read_messages=True)
            }
        # check which button was pressed, then create new channel, send embed, give confirmation. and yeah i'm not using a switch, I'm eepy and this is fine
        try:
            if inter.data["custom_id"] == "0":    
                channel = await category.create_text_channel(name=f'{inter.user}-attorney-request', topic="Attorney Request Ticket", overwrites=overwrites)
                await TicketEmbed.ticket_embed(channel)
                await inter.send(f'Ticket created successfully', ephemeral=True)

            elif inter.data["custom_id"] == "1":
                channel = await category.create_text_channel(name=f'{inter.user}-client-request', topic="S&C Client Request Ticket", overwrites=overwrites)
                await TicketEmbed.ticket_embed(channel)
                await inter.send(f'Ticket created successfully', ephemeral=True)

            elif inter.data["custom_id"] == "2":
                channel = await category.create_text_channel(name=f'{inter.user}-employment-application', topic="Employment Request Ticket", overwrites=overwrites)
                await TicketEmbed.ticket_embed(channel)
                await inter.send(f'Ticket created successfully', ephemeral=True)

            elif inter.data["custom_id"] == "3":   
                channel = await category.create_text_channel(name=f'{inter.user}-feedback', topic="Provide feedback to Ryan and Fred", overwrites=overwrites)
                await TicketEmbed.ticket_embed(channel)
                await inter.send(f'Ticket created successfully', ephemeral=True)

            elif inter.data["custom_id"] == "4":   
                channel = await category.create_text_channel(name=f'{inter.user}-role-request', topic="Role Request Ticket", overwrites=overwrites)
                await TicketEmbed.ticket_embed(channel)
                await inter.send(f'Ticket created successfully', ephemeral=True)                    
        except:
            print('Event Logged')

def setup(bot: commands.Bot) -> None:
    bot.add_cog(TicketRequestButton(bot))