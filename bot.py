import discord, aiohttp, asyncio, sys, time
from discord.ext import commands
from discord.ext import tasks
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses, snowstamp, purge_list, models
import datetime
from datetime import datetime, timedelta
import threading
intents = discord.Intents.all()
client = discord.Client(intents = intents)



@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

async def scheduledEvent():
  threading.Timer(1, scheduledEvent).start()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  # print("Current Time =", current_time)
  # comment that out to not pollute the console; otherwise will fire every one second
  if(current_time == '09:41:00'):  # check if matches with the desired time
    then = datetime.now() - timedelta(days = 7)
    print(f"it is now {current_time}") # this code block is no longer running. may want to touch back later.
    mem_list = list()
    role = "onboarding complete" # name of the default role of all users that complete onboarding
    purge_list = list()
    for member in client.get_all_members():
      mem_list.append({"id": member.id, "name": member.name, "messages_sent": 0, "roles": member.roles, "join_date": member.joined_at})
      # add these to the discord user list if they're not already there
      # subtract any users from the db whose ids are not present in the list; they've left the server
    for value in mem_list:
      if role in str(value["roles"]):
        print(f'{str(value["name"])} has completed onboarding')
        # set onboarding_complete in db to true
    for value in mem_list:
        if role not in (str(value["roles"])) and member.joined_at.timestamp() < then.timestamp():
          purge_list.append(value)
          print(f'{str(value["id"])} {str(value["name"])} has not completed onboarding after one week')
          for member in purge_list:
            # can't get this line of code to kick a member right
            print(f'{member["id"]} kicked')
            x = client.fetch_user(member["id"])
            client.kick(x, reason = "never onboarded")
            # add them to the new table 'has been kicked previously' in the db
            # may expand upon this in the future

            # wait what is all this?? this looks like the kick functionality but it doesn't work yet.
            # i need to send the purge_list stuff to the actual purge list via sqlalchemy queries.
            # so let's get the kick functionality to work, then worry about sending it to the db
            # make a function only callable by administrators to get a list of kickable users,
            # just to be on the safe side, so that a mod can review it for testing/safety/not kicking everyone at once.
            # so i can't seem to take scheduled event and put it in another file because of a runtime warning but also it's not currently doing anything.


  await scheduledEvent()

async def setup_hook(self) -> None:
    self.alarm_message.start()

@tasks.loop(minutes = 1)

async def alarm_message():
    await client.wait_until_ready()
    channel = client.get_channel(1043014753875939389) # it's been a while since i messed with this; should have commented it back then but i believe this is for the specific discord server (my bot test server)
    message = 'test'
    # await channel.send(message)
    await print(message)
    await alarm_message.start()



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
    await message.channel.send(x) # allows any number be passed as argument
  if msg.startswith("/curse"):
    await message.channel.send(chat_curses.curse_generator())
    
  
  admins = [145031705303056384, 257032548431953922, 217569769052700672] # make sure only admin ids go here
  
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

  # this should be in its own function; it's to check user activity levels.

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
    role = msg.guild.get_role(1079214033036660797) #need to get the specific role for specific server; this role is outdated
    #okay this works, now you need to have a time function to remove the role if less than 10 messages.
    await msg.author.add_roles(role, reason=None, atomic=True)
    # after this print statement, you can append priveleged role status to sql database
    # via sqlalchemy
    # then, every so often, check the sql database to change roles

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)

# models.connect_db(app)