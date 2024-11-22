from nextcord.ext.commands import Bot

# retrieve token from 100% secure file format
with open("token.txt") as file:
    token = file.read()

# the bot is now botting
bot = Bot()

# load ticket creation cogs
bot.load_extension("cogs.attorneyrequest")
bot.load_extension("cogs.clientticket")
bot.load_extension("cogs.employmentapp")
bot.load_extension("cogs.feedback")
bot.load_extension("cogs.rolerequest")
bot.load_extension('cogs.buttons')

# load ticket management cogs
bot.load_extension("cogs.rename")

# load misc cogs
bot.load_extension("cogs.ping")
bot.load_extension("cogs.nat")

# blast off
bot.run(token)