import discord, aiohttp, asyncio, sys, time
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses, snowstamp
import datetime
from datetime import datetime, timedelta
intents = discord.Intents.all()
client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

  counter = 0
  mem_list = list()
  role = "gay gay homosexual gay"
  purge_list = list()
  for member in client.get_all_members():
    mem_list.append({"id": member.id, "name": member.name, "messages_sent": 0, "roles": member.roles, "join_date": member.joined_at})
  for value in mem_list:
    if role in str(value["roles"]):
      print(str(value["name"]))
      # okay so that prints the role only when the user has the role.
      # now we need to check if their join date is 7 days prior
      # and if so, purge them.
      # then loop the part of the on_ready function that checks that.

  # print(mem_list) #that'll give you a lot of members with a lot of information
  #since you know that works, you don't need to print it every time now.

    # push the member id to a table using sqlalchemy
    # the table should have member id, member name, and number of messages sent within 144 hours  

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
  if msg.startswith("/d20"):
    await message.channel.send(d20.d20())
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
  print(message.author.name)
  print(f'in {c_col}{message.channel.name}, {m_col}{message.author.name}{tc.W}:')
  print(message.content)
  print(snowstamp.createTimestamp(message.id))
  counter = 0
  idList = []
  then = datetime.now() - timedelta(days = 7)
  for channel in message.guild.text_channels:
    async for msg in channel.history(after = then):
      # put one week back from now using timedelta or snowflake in the history param
      # you'll want to flatten that output into a list of dicts with timestamps
      # and check the timestamp of the tenth message against the timestamp of the first message
      if msg.author == message.author:
        # print(msg.id)
        if len(idList) < 10:
          idList.append(msg.id)
        else:
          break
          # now compare the unix timestamps of the last message to the first message
        counter += 1
  # print(counter)
  # print(idList) # hiding this for now because tired of long list printing in terminal
  if counter >= 10:
    print("congratulations, you're granted a priveleged role!")
    # after this print statement, you can append priveleged role status to sql database
    # via sqlalchemy
    # then, every so often, check the sql database to change roles

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)