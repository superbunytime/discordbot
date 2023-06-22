import discord, aiohttp, asyncio, sys, time
from discord.ext import commands, tasks
import text_coloring as tc
import tarot, d20, chat_curses, snowstamp
import datetime
from datetime import datetime, timedelta
import threading
import sqlalchemy
from sqlalchemy import BigInteger, Column, Integer, create_engine, String, Integer, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
import queries, models
intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  mem_builder.start()

@tasks.loop(seconds=10.0)
async def mem_builder():
  mem_list = list()
  members = []
  kickable = []
  then = datetime.now() - timedelta(days = 7)
  for member in client.get_all_members():
    if len(member.roles) < 2 and member.joined_at.timestamp() > then.timestamp():
      await member.kick(reason="never onboarded")
      kickable.append({"id": member.id,
                    "name": member.name,
                    "roles": len(member.roles) < 2,
                    "joined_at": member.joined_at})
      # for polish, add these to the has_not_onboarded table
      # for now, just make sure they meet all the requirements to be kicked,
      # and kick them.
  # print(kickable)
  for member in kickable:
    print(member["id"])
    # okay that gets the id, now kick them.
    # oops none of that was working so i just kicked them up on line 29 and that worked.
    
  for member in client.get_all_members():
    # for some reason it was giving me an error until i restarted the same for loop
    # I'm sure it's something simple, but for now I'm just going to redeclare it.
    members.append({"id": member.id,
                    "name": member.name,
                    "roles": len(member.roles) >= 2,
                    "joined_at": member.joined_at})
  for member in members:
    new_user = models.USER(id = member['id'], name = member['name'], has_roles = member['roles'], join_date = member['joined_at'].strftime("%c"))
    mem_list.append(new_user)

  queries.add_to_db(mem_list)
  # looking at upsert stuff, wouldn't it be easier for now to just drop the table and rebuild it completely?  it may be computationally heavy, but we can always worry about upsert stuff when we're doing polish.

@client.event
async def on_message(message):

  # if message.author == client.user:
  #   return
    # if this is commented out, make sure nothing causes the bot to reply to itself
    # as this would immediately cause an infinite loop and crash the program

  msg = message.content
  msgl = message.content.lower()

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
  # check for default uncolored users.
  if member_col == discord.Colour.default():
    # render them as white instead of black.
    m_col = tc.W
  else:
    m_col = tc.new(member_col.r, member_col.g, member_col.b)
  c_col = tc.new(255,82,197) if not message.channel.nsfw else tc.R
  print(f'this is the channel id: {message.channel.id}')
  print(message.author.name)
  print(f'in {c_col}{message.channel.name}, {m_col}{message.author.name}{tc.W}:')
  print(message.content)
  print(snowstamp.createTimestamp(message.id))

  # this should be in its own function; it's to check user activity levels.

  # so this code block was being used to track if users are active or not.  I can repurpose this to interact with the database.
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