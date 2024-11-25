import nextcord
import os
import time
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

        # continue with command if channel is a ticket
        if channel_category == ticket_category:
            # send confirmation that ticket is transcripting
            await TicketEmbed.ticket_transcript_embed(channel=channel, ticket_name=channel_name)

            try:
                # get all messages in channel, format as html file
                message_history = await channel.history(limit=None).flatten()
                message_history.reverse()
                html_messages = self.format_to_html(message_history)

                # Save history
                file_name = f"{channel_name}_{date.today()}.html"
                transcript_folder_path = "/home/ryan/Documents/PythonProjects/SCTicketBot/transcripts" # TODO redefine path

                # If transcript folder does not exist, make it exist
                if not os.path.exists(transcript_folder_path):
                    os.makedirs(transcript_folder_path)

                # write to file
                file_path = os.path.join(transcript_folder_path, file_name)
                with open(file_path, 'w') as file:
                    file.write(html_messages)

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
    
    def format_to_html(self, messages):
        html_content = """
        <html>
        <head>
            <style>
                body {background-color: #36393e; color: white; font-family: gg-sans;}
                .message { margin: 10px; padding: 10px; border: 1px solid #555; border-radius: 5px; }
                .author { font-weight: bold; color: white; }
                .embed { border: 1px solid #555; background-color: #424549; margin: 10px; padding: 10px; border-radius: 5px; }
                .embed-title { font-weight: bold; font-size: 1.2em; }
                .embed-description { margin-top: 5px; }
                .embed-field { margin-top: 10px; }
                .embed-field-name { font-weight: bold; }
                .embed-field-value { margin-left: 10px; }
            </style>
        </head>
        <body>
        """
        for message in messages:
            html_content += f"<div class='message'><p><span class='author'>{message.author}:</span> {message.content}</p>"

            # do embeds
            for embed in message.embeds:
                html_content += self.format_embed_to_html(embed)

            html_content += "</div>"

        html_content += "</body></html>"
        return html_content

    def format_embed_to_html(self, embed):
        embed_html = "<div class='embed'>"
        if embed.title:
            embed_html += f"<div class='embed-title'>{embed.title}</div>"
        if embed.description:
            embed_html += f"<div class='embed-description'>{embed.description}</div>"
        for field in embed.fields:
            embed_html += f"<div class='embed-field'><span class='embed-field-name'>{field.name}:</span> <span class='embed-field-value'>{field.value}</span></div>"
        if embed.image:
            embed_html += f"<img src='{embed.image.url}' alt='Embed Image' style='max-width: 100%; margin-top: 10px;' />"
        if embed.thumbnail:
            embed_html += f"<img src='{embed.thumbnail.url}' alt='Embed Thumbnail' style='float: right; margin: 10px;' />"
        embed_html += "</div>"
        return embed_html

def setup(bot) -> None:
    bot.add_cog(Transcript(bot))
