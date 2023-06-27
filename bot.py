import discord, aiohttp, asyncio, sys, time, yaml
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

with open('personalconfig.yml', 'r') as file:
  config = yaml.safe_load(file)
  # for deployment, change personalconfig.yml to config.yml
  # I still need to run my own instances of the bot, hence the personalconfig.yml

intents = discord.Intents.all()
client = discord.Client(intents = intents)

"""@client.event and @tasks.loop run the database and non-onboarded kicking features"""

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  mem_builder.start()

@tasks.loop(seconds=config["TASKS_LOOP"])
async def mem_builder():
  if config["ENABLE_KICKING"]:
    mem_list = list()
    members = []
    kickable = list()
    mem_read_from_db = []
    then = datetime.now() - timedelta(days = 7)
    for member in client.get_all_members():
      if len(member.roles) < 2 and member.joined_at.timestamp() > then.timestamp():
        await member.kick(reason="never onboarded")
        kickable.append({"id": member.id,
                      "name": member.name,
                      "roles": len(member.roles) < 2,
                      "joined_at": member.joined_at})
      
    for member in client.get_all_members():
      members.append({"id": member.id,
                      "name": member.name,
                      "roles": len(member.roles) >= 2,
                      "joined_at": member.joined_at})
    for member in members:
      new_user = models.USER(id = member['id'], name = member['name'], has_roles = member['roles'], join_date = member['joined_at'].strftime("%c"))
      mem_list.append(new_user)

    queries.add_to_db(mem_list)
    queries.add_to_kick_db(kickable)
    queries.read_from_db(mem_read_from_db)

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
      
  admins = config["ADMIN"]

  if msgl in ["kill bot", "stop bot", "bot die", "bot stfu", "]"] and message.author.id in admins:
    await message.channel.send("OOF")
    quit() # warning: this will kill the bot across all servers it's in. only use this in case of emergencies. in fact, don't actually use this at all. don't look at this method, forget it exists.
  
  """text coloring for terminal feed"""

  member_col = message.author.color
  # check for default uncolored users.
  if member_col == discord.Colour.default():
    # render them as white instead of black.
    m_col = tc.W
  else:
    m_col = tc.new(member_col.r, member_col.g, member_col.b)
  c_col = tc.new(255,82,197) if not message.channel.nsfw else tc.R
  print(f'in {c_col}{message.channel.name}, {m_col}{message.author.name}{tc.W}:')
  print(message.content)

  """VIP role functionality:
  Checks user activity level on a rolling x day window"""

  if config["ENABLE_VIP"]:
    counter = 0
    idList = []
    then = datetime.now() - timedelta(seconds = config["TASKS_INACTIVE_TIMER"])
    for channel in message.guild.text_channels:
      async for msg in channel.history(after = then):
        if msg.author == message.author:
          if len(idList) < config["VIP_MESSAGES"]:
            idList.append(msg.id)
          else:
            break
          counter += 1
    if counter >= 10:
      role = msg.guild.get_role(config["VIP_ROLE"])
      await msg.author.add_roles(role, reason=None, atomic=True)
    else:
      role = msg.guild.get_role(config["VIP_ROLE"])
      await msg.author.remove_roles(role, reason=None, atomic=True)


with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)