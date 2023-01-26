import discord, os, random_fursona, tarot, d20, chat_curses, botlogic, aiohttp, asyncio, sys, time

  
intents = discord.Intents.all()
client = discord.Client(intents = intents)
@client.event
# async def on_ready():
#   print("we have logged in as {0.user}".format(client))

#   mem_set = set()
#   counter = 0
#   for member in client.get_all_members():
#     mem_set.add(member.id)
    
#   mem_dict = dict.fromkeys(mem_set, counter)

#   print(mem_dict) #that'll give you a lot of members with a lot of information


    # push the member id to a table using sqlalchemy
    # the table should have member id, member name, and number of messages sent within 144 hours  
    
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msgl = message.content.lower()

  if msg.startswith("/fursona"):
    await message.channel.send(random_fursona.fursona_generator())
  if msg.startswith("/tarot"):
    await message.channel.send(tarot.tarot_generator())
  if msg.startswith("/d20"):
    await message.channel.send(d20.d20())
  if msg.startswith("/curse"):
    await message.channel.send(chat_curses.curse_generator())
  
  # print(message.author.id)
  print(f'channel: {message.channel.name}')
  print(f'user: {message.author.name}')
  print(message.content)

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)