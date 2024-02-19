import discord, aiohttp, asyncio, sys, time
from discord.ext import commands, tasks
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses, chat_blessings, md_flagger
import datetime
from datetime import datetime, timedelta


intents = discord.Intents.all()
client = discord.Client(intents = intents)

bless_duration_list = list()
member_set = set()

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  mem_builder.start()
  toilet_cleaning.start()
  
# test for value already existing in bless duration list
  for member in client.get_all_members():
    member_set.add(member.name)
  
  for member in member_set:
    bless_duration_list.append({"name":member, "blessing":'blessing refactory period',"duration":1, "timestamp":datetime.now().timestamp()})
  print(bless_duration_list)


@tasks.loop(seconds = 172800)
async def toilet_cleaning():
  toilet = client.get_channel(1007471133207035934)
  messages = toilet.history(limit=99)
  then = datetime.now() - timedelta(seconds = 172800)
  async for m in messages:
    if m.created_at.timestamp() < then.timestamp():
      await asyncio.sleep(3)
      await m.delete()

      # set loop timer, channel id, limit threshold, and timedelta values before deploying

@tasks.loop(seconds = 86400)
async def mem_builder():
    mem_list = list()
    members = []
    kickable = list()
    mem_read_from_db = []
    then = datetime.now() - timedelta(days = 7)
    yesterday = datetime.now() - timedelta(minutes = 1)

    for member in client.get_all_members():
      if len(member.roles) < 2 and member.joined_at.timestamp() < then.timestamp():
        # print(f'{member.name} ({member.id}) should probably be kicked from the server. They joined at {member.joined_at.strftime("%c")}, and still have not completed onboarding.')
        print(member.id)
        # await member.kick(reason="never onboarded")
        # uncomment to kick member that hasn't onboarded.


    # for member in client.get_all_members():
    #   members.append({"id": member.id,
    #                   "name": member.name,
    #                   "roles": len(member.roles) >= 2,
    #                   "joined_at": member.joined_at})
    # for member in members:
    #   new_user = models.USER(id = member['id'], name = member['name'], has_roles = member['roles'], join_date = member['joined_at'].strftime("%c"))
    #   mem_list.append(new_user)

    # for member in queries.read_from_db(mem_read_from_db):
    #   u = models.USER(id = member['id'], name = member['name'], has_roles = member['has_roles'], join_date = member['join_date'].strftime("%c"))
    #   if u.has_roles == "false" and datetime.strptime(u.join_date, "%c").timestamp() > then.timestamp():
    #     kickable.append(int(u.id))
    # for member in client.get_all_members():
    #     if member.id in kickable:
    #       await member.kick(reason="never onboarded")

    # queries.add_to_db(mem_list)

embeds_list = []

@client.event
async def on_message(message):

  if message.author == client.user:
    print(f'in {message.channel.name}, {message.author.name}')
    print(message.content)
    return
    # if this is commented out, make sure nothing causes the bot to reply to itself
    # as this would immediately cause an infinite loop and crash the program

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
  if msg.startswith("/bless"):
    for item in bless_duration_list:
      if message.author.name in item["name"]:
        then_after = item["timestamp"] + (item["duration"] * 60)
        if datetime.now().timestamp() < then_after:
          await message.channel.send(f'{message.author.name}, your previous bless, *{item["blessing"]}* is still active! duration: {item["duration"]} minutes. Time remaining: {int(then_after) - int(datetime.now().timestamp())} seconds... hopefully.')
          break
        if datetime.now().timestamp() > then_after:
          # delete item
          bless_duration_list.remove(item)
          # add new item
          bless_obj = chat_blessings.bless_generator()
          bless_duration_list.append({"name":message.author.name, "blessing":bless_obj[0], "duration":bless_obj[1], "timestamp":message.created_at.timestamp()})
          await message.channel.send(f"you have been blessed with {bless_obj[0]} for {bless_obj[1]} minutes!")
          break
          # anyway this stuff gets funky if your bot is in multiple servers you're also in
          # which was my case with the test branch stuff.
          # which btw i've been committing to the polish branch for some reason???
          # if this works i'm gonna git commit so hard my whole bloodline will feel it


      
#   admins = config["ADMIN"]

#   if msgl in ["kill bot", "stop bot", "bot die", "bot stfu", "]"] and message.author.id in admins:
#     await message.channel.send("OOF")
#     quit() # warning: this will kill the bot across all servers it's in. only use this in case of emergencies. in fact, don't actually use this at all. don't look at this method, forget it exists.
  
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

  """malicious embed user protection"""
  role = discord.utils.get(message.guild.roles, name = "Subby Wubby")
  mod_role = discord.utils.get(message.guild.roles, name = "Mods")
  bot_role = discord.utils.get(message.guild.roles, name = "Bots")
  if 'http' in message.content and role not in message.author.roles: # the one line of code that got it all working.
    embeds_list.append(message)
    # print('http detected; deploying neurotoxin')
  for m in embeds_list:
    then_again = int(datetime.now().timestamp())  # set the actual desired time
    creation_ts = int(m.created_at.timestamp()) + 234000 # this is the line where you change the time

    if creation_ts < then_again and hasattr(m, 'content'):
      try:
        await m.delete()
        embeds_list.remove(m)
      except:
        print("something went wrong deleting, oopsy.")

  """Malicious markdown detection and warning systme"""
  # somewhat concerned why bot would flag twice on samantha and only once on adramalechk
  # but it works so whatever

  if md_flagger.md_flagger(message.content) and not hasattr(message.author, 'roles'):
    if role not in message.author.roles and mod_role not in message.author.roles:
      await message.channel.send("Warning! Potentially malicious embedded link")

  """VIP role functionality:
  Checks user activity level on a rolling x day window"""

#   if config["ENABLE_VIP"]:
#     counter = 0
#     idList = []
#     then = datetime.now() - timedelta(seconds = config["TASKS_INACTIVE_TIMER"])
#     for channel in message.guild.text_channels:
#       async for msg in channel.history(after = then):
#         if msg.author == message.author:
#           if len(idList) < config["VIP_MESSAGES"]:
#             idList.append(msg.id)
#           else:
#             break
#           counter += 1
#     if counter >= 10:
#       role = msg.guild.get_role(config["VIP_ROLE"])
#       await msg.author.add_roles(role, reason=None, atomic=True)
#     else:
#       role = msg.guild.get_role(config["VIP_ROLE"])
#       await msg.author.remove_roles(role, reason=None, atomic=True)


with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)