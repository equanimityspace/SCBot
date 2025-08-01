import nextcord
import os
import time
import io
import chat_exporter
from nextcord import Interaction, slash_command
from nextcord.ui import Button, View
from nextcord.ext.commands import Bot, Cog
from datetime import date

class TicketEmbed():
    @staticmethod
    # create embed
    async def ticket_transcript_embed(channel, ticket_name) -> None:
        embed = nextcord.Embed(title=f'Creating transcript of {ticket_name}...', color=15902030)
        await channel.send(embed=embed)

class TranscriptEmbed():
    @staticmethod
    # create embed
    async def ticket_embed(log_channel, ticket_name) -> None:
        embed = nextcord.Embed(title=f'{ticket_name}', description="Transcript Link", color=2995633)
        await log_channel.send(embed=embed)

class CloseEmbed():
    @staticmethod
    # create embed
    async def ticket_close_embed(channel) -> None:
        embed = nextcord.Embed(title='Transcript saved, ticket closing...', color=12194065)
        await channel.send(embed=embed)

# Begin transcript process with /close
class Transcript(Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @slash_command(name="close", description="Transcript and close the current ticket")
    async def transcript_close(self, inter: Interaction) -> None:
        # get current channel category, then category that tickets go in\
        channel = inter.channel
        channel_name = channel.name
        channel_category = inter.channel.category_id
        guild = inter.guild
        ticket_category = 1309294281034301552 # TODO fix ticket category int
        log_channel = guild.get_channel(1309294488438702080)
        channel_link = channel.jump_url

        # continue with command if channel is a ticket
        if channel_category == ticket_category:
            # send confirmation that ticket is transcripting
            await TicketEmbed.ticket_transcript_embed(channel=channel, ticket_name=channel_name)

            try:
                transcript = await chat_exporter.export(
                    channel,
                    tz_info="America/Detroit",
                    fancy_times=True,
                )

                if transcript is None:
                    return

                # Save history
                file_name = f'transcript-{channel_name}.html'
                transcript_folder_path = "/home/ryan/Documents/PythonProjects/SCTicketBot/transcripts" # TODO redefine path

                # If transcript folder does not exist, make it exist
                if not os.path.exists(transcript_folder_path):
                    os.makedirs(transcript_folder_path)

                # write to file
                file_path = os.path.join(transcript_folder_path, file_name)
                with open(file_path, 'w') as file:
                    file.write(transcript)

                # create embed with link to file
                await TranscriptEmbed.ticket_embed(log_channel=log_channel, ticket_name=channel_name)
            except Exception as e:
                await channel.send("<@185405006751596545> Transcript failed, cancelling...")
                print(f'Error transcripting:\n{e}')
                return

            # delete channel
            await CloseEmbed.ticket_close_embed(channel=channel)
            time.sleep(3)
            await channel.delete()
        else:
            await channel.send("This channel is not a ticket", ephemeral=True)

def setup(bot) -> None:
    bot.add_cog(Transcript(bot))