import discord
import os
import random_fursona

intents = discord.Intents.all()
client = discord.Client(intents = intents)
@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msgl = message.content.lower()

  if msg.startswith("?hello"):
    await message.channel.send("hi")
  if msg.startswith("?fursona"):
    await message.channel.send(random_fursona.fursona_generator())

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)