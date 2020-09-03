import discord
import asyncio
import requests
import os
from discord.ext.commands import Bot

# tokens

discord_token = 'DISCORD_TOKEN_HERE'
channel_id = 'CHANNEL_ID_HERE'


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):

	print("**{}** has joined the server".format(member.name))

	channels = ["join-leaves"]

	msg = "**{}** has joined the server".format(member.name)

	channel = client.get_channel(channel_id)
	await channel.send(msg)

@client.event
async def on_member_remove(member):

	print("**{}** has left the server".format(member.name))

	channels = ["join-leaves"]

	msg = "**{}** has left the server".format(member.name)

	channel = client.get_channel(channel_id)
	await channel.send(msg)

client.run(discord_token)
