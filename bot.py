import discord, aiohttp, asyncio, sys, time
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses, snowstamp
import datetime
from datetime import datetime, timedelta
import threading
intents = discord.Intents.all()
client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  then = datetime.now() - timedelta(days = 7)
  mem_list = list()
  role = "gay gay homosexual gay" # name of the default role of all users that complete onboarding
  purge_list = list()
  for member in client.get_all_members():
    mem_list.append({"id": member.id, "name": member.name, "messages_sent": 0, "roles": member.roles, "join_date": member.joined_at})
  for value in mem_list:
    if role in str(value["roles"]):
      print(f'{str(value["name"])} has completed onboarding')

  # print(mem_list) #that'll give you a lot of members with a lot of information
  for value in mem_list:
      if role not in (str(value["roles"])) and member.joined_at.timestamp() < then.timestamp():
        purge_list.append(value)
        print(f'{str(value["name"])} has not completed onboarding after one week')
  print(purge_list)
    # push the member id to a table using sqlalchemy
    # the table should have member id, member name, and number of messages sent within 144 hours  

  def checkTime():
  # This function runs periodically every 1 second
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)
    # comment that out to not pollute the console

    if(current_time == '23:39:30'):  # check if matches with the desired time
        print('sending message')
        # make a function and have it called here


  checkTime()

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
  # print(message.guild.id)
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
    # print("congratulations, you're granted a priveleged role!")
    role = msg.guild.get_role(1079214033036660797) #need to get the specific role for specific server
    #okay this works, now you need to have a time function to remove the role if less than 10 messages.
    await msg.author.add_roles(role, reason=None, atomic=True)
    # after this print statement, you can append priveleged role status to sql database
    # via sqlalchemy
    # then, every so often, check the sql database to change roles

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)