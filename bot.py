import discord, os, random_fursona, tarot, d20, chat_curses, botlogic, aiohttp, asyncio, sys, time

  
intents = discord.Intents.all()
client = discord.Client(intents = intents)
@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  # for member in client.get_all_members():
  #   print(member.id)
    # push the member id to a table using sqlalchemy
    # the table should have member id, member name, and number of messages sent within 144 hours
  print(botlogic.member_list(botlogic.set1))
    


@client.event
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
  
  print(message.author.id)
  if message.author.id == botlogic.cinnabun.id:
    botlogic.cinnabun.msgCount +=1
    print(botlogic.cinnabun.msgCount)



with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)