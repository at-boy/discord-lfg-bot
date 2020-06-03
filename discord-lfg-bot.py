import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!?lfg'):
        await message.channel.send( '<@!' + str(message.author.id) + '>' + ' let me help you with that\n\n\t__If you are looking for games that needs players:__ **!?lfg listgames**\n\n\t__If you are looking for players for your game:__ **!?lfg listplayers**\n\n\t__If you want to announce that you are interested in joining groups:__ **!?lfg announce-me**\n\n\t__If you want to announce and create a new game:__ **!?lfg new-game**')

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client.run(DISCORD_BOT_TOKEN)
