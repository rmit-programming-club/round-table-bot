import discord
import random
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

dating_circle = set()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$join'):
        dating_circle.add(message.author)
        await message.channel.send('You have joined the meetup group')

    if message.content.startswith('$match'):
        shuffled = list(dating_circle)
        random.shuffle(shuffled)
        matches = len(shuffled) // 2
        await message.channel.send('Here are the pairs')
        for i in range(matches):
            await message.channel.send(shuffled[i * 2].mention  + ' is matched to ' + shuffled[i * 2 + 1].mention)

        if matches * 2 != len(shuffled):
            await message.channel.send(shuffled[-1].mention  + ' was not matched')

client.run(sys.env['DISCORD_TOKEN'])

