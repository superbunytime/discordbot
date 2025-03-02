import discord, asyncio
from discord.ext import commands, tasks
import datetime
from datetime import datetime, timedelta
import text_coloring as tc
import random_fursona, tarot, puppytarot, d20, chat_curses, chat_blessings, soapstone, md_flagger, barkanadefinitions


intents = discord.Intents.all()
client = discord.Client(intents = intents)

bless_duration_list = list()
member_set = set()

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  toilet_cleaning.start()

@tasks.loop(seconds = 172800)
async def toilet_cleaning():
  toilet = client.get_channel(1136784026666008636)
  messages = toilet.history(limit=99)
  then = datetime.now() - timedelta(seconds = 172800)
  async for m in messages:
    if m.created_at.timestamp() < then.timestamp():
      await asyncio.sleep(3)
      await m.delete()
async def bless_refresher():
  for member in client.get_all_members():
    member_set.add(member.name)
  
  for member in member_set:
    bless_duration_list.append({"name":member, "blessing":'blessing refactory period',"duration":1, "timestamp":datetime.now().timestamp()})
  print(bless_duration_list)



      # set loop timer, channel id, limit threshold, and timedelta values before deploying

embeds_list = []

@client.event
async def on_message(message):
  # if message.author == client.user:
  #   return
    #if this is commented out, make sure nothing causes the bot to reply to itself
    #as this would immediately cause an infinite loop and crash the program

  msg = message.content
  msgl = message.content.lower()

  if msg.startswith("/fursona") and not message.author.bot:
    await message.channel.send(random_fursona.fursona_generator())
  if msg.startswith("/tarot") and not message.author.bot:
    number_of_cards = 1
    deck_position = 0
    deck_position_text = "top"
    if "top" in msg:
      deck_position = 0
      deck_position_text = "top"
    if "middle" in msg:
      deck_position = 48
      deck_position_text = "middle"
    if "bottom" in msg:
      deck_position = -1
      deck_position_text = "bottom"
    print(msg[9:10].isnumeric())
    for x in msg:
      if x.isnumeric() and int(x) > 0:
        number_of_cards = int(x)
    await message.channel.send(tarot.tarot_generator(number_of_cards, deck_position, deck_position_text))

  if msg.startswith("/barkana") and not message.author.bot:
    number_of_cards = 1
    deck_position = 0
    deck_position_text = "top"
    if "top" in msg:
      deck_position = 0
      deck_position_text = "top"
    if "middle" in msg:
      deck_position = 48
      deck_position_text = "middle"
    if "bottom" in msg:
      deck_position = -1
      deck_position_text = "bottom"
    print(msg[9:10].isnumeric())
    for x in msg:
      if x.isnumeric() and int(x) > 0:
        number_of_cards = int(x)
    await message.channel.send(puppytarot.barkana_generator(number_of_cards, deck_position, deck_position_text))
  if msg.startswith("/explainbarkana") and not message.author.bot:
    # channel = await message.author.create_dm()
    # await channel.send("code to send explanation goes here.") # this will allow you to send a dm to the user through the bot with an explanation, but an ephemeral message would be better. those can only be accomplished through reaction listening though. will work on that at a later date.
    if "suits" in msg:
      await message.channel.send(barkanadefinitions.suits)
    if "ranks" in msg:
      await message.channel.send(barkanadefinitions.ranks)
    if "tips" in msg:
      await message.channel.send(barkanadefinitions.tips)
    # if str(msg[16:]) in puppytarot.tarot_list:
      # alright this hits a match if it's in the barkana array
      # now we need to make them into different structures and it's going to slightly confuse things because they need to have a name and an explanation.

  if msg.startswith("/d") and type(int(msg[2:])) == int and not message.author.bot:
    x = d20.d(int(msg[2:]))
    await message.channel.send(x)
  if msg.startswith("/soapstone") and not message.author.bot:
    await message.channel.send(soapstone.MessageFactory().message())
  if msg.startswith("/curse") and not message.author.bot:
    await message.channel.send(chat_curses.curse_generator())
  if msg.startswith("/bless") and not message.author.bot:
    for item in bless_duration_list:
      if message.author.name in item["name"]:
        then_after = item["timestamp"] + (item["duration"] * 60)
        if datetime.utcnow().timestamp() < then_after:
          await message.channel.send(f'{message.author.name}, your previous bless, *{item["blessing"]}* is still active! duration: {item["duration"]} minutes. Time remaining: {int(then_after) - int(datetime.utcnow().timestamp())} seconds... hopefully.')
          break
        if datetime.utcnow().timestamp() > then_after:
          # delete item
          bless_duration_list.remove(item)
          # add new item
          bless_obj = chat_blessings.bless_generator()
          bless_duration_list.append({"name":message.author.name, "blessing":bless_obj[0], "duration":bless_obj[1], "timestamp":message.created_at.timestamp()})
          await message.channel.send(f"you have been blessed with {bless_obj[0]} for {bless_obj[1]} minutes!")
          break
          # anyway this stuff gets funky if your bot is in multiple servers you're also in
          # which was my case with the test branch stuff.

  if "-#" in message.content and 'https://' in message.content or msg.startswith("-#") and 'http://' in message.content:
    await message.channel.send("Warning: The preceding message may contain a phishing link")
    
  
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

  if md_flagger.md_flagger(message.content) and not hasattr(message.author, 'roles'):
    if role not in message.author.roles and mod_role not in message.author.roles and not message.author.bot:
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