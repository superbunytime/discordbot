import discord, aiohttp, asyncio, sys, time
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses

intents = discord.Intents.all()
client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))



@client.event
async def on_message(message):
  # if message.author == client.user:
  #   return
    #if this is commented out, make sure nothing causes the bot to reply to itself
    #as this would immediately cause an infinite loop and crash the program

  msg = message.content
  msgl = message.content.lower()

  if msg.startswith("/fursona"):
    await message.channel.send(random_fursona.fursona_generator())
  if msg.startswith("/tarot"):
    await message.channel.send(tarot.tarot_generator())
  if msg.startswith("/d") and type(int(msg[2:])) == int:
    x = d20.d(int(msg[2:]))
    await message.channel.send(x)
  if msg.startswith("/curse"):
    await message.channel.send(chat_curses.curse_generator())
  
  #butte, puppy, bunny
  admins = [145031705303056384, 257032548431953922, 217569769052700672]
  
  if msgl in ["kill bot", "stop bot", "bot die", "bot stfu", "]"] and message.author.id in admins:
    await message.channel.send("OOF")
    quit()
  
  
  member_col = message.author.color
  #check for default uncolored users.
  if member_col == discord.Colour.default():
    #render them as white instead of black.
    m_col = tc.W
  else:
    m_col = tc.new(member_col.r, member_col.g, member_col.b)
  c_col = tc.new(255,82,197) if not message.channel.nsfw else tc.R
  print(f'in {c_col}{message.channel.name}, {m_col}{message.author.name}{tc.W}:')
  print(message.content)

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)