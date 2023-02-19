import discord, aiohttp, asyncio, sys, time
import text_coloring as tc
import random_fursona, tarot, d20, chat_curses, botlogic

intents = discord.Intents.all()
client = discord.Client(intents = intents)


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

  counter = 0
  mem_list = list()
  for member in client.get_all_members():
    mem_list.append({"id": member.id, "name": member.name, "messages_sent": 0})
    

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
  print(f'in {c_col}{message.channel.name}, {m_col}{message.author.name}{tc.W}:')
  print(message.content)
  counter = 0
  for channel in message.guild.text_channels:
    async for msg in channel.history(limit = 10):
      # you'll want to flatten that output into a list of dicts with timestamps
      # and check the timestamp of the tenth message against the timestamp of the first message
      if msg.author == message.author:
        print(msg.content)
        counter += 1
  print(counter)
  if counter >= 10:
    print("congratulations, you're granted a priveleged role!")
    # after this print statement, you can append priveleged role status to sql database
    # via sqlalchemy
    # then, every so often, check the sql database to change roles

  # so that counts all the messages sent by a user in a channel. (maybe all users, let's check manually)
  # so it reaches back 3 months into discord message history, which is more than enough for our purposes
  # now you just need to check *all* channels for messages from the user, which means putting it in
  # an inefficient for loop
  # and if you can time-constraint it to a week, you won't have to use timedelta either

# @client.event
# async def history(ctx, member: discord.member):
#   messages = []
#   async for channel in ctx.guild.channels:
#     for message in ctx.channel.history(limit=None):
#       if message.author.id == member.id:
#         messages += [message]

# Or...

# messages = [msg for msg in await ctx.channel.history(limit=100).flatten() if msg.author.id == memberID]
  # for m in message.author.history(limit =10):
  #   print(m)
  # okay that just breaks it (attempt 2)
  # in case you lose the link go here:
  # https://stackoverflow.com/questions/65560383/how-to-get-all-messages-that-user-sent-in-server-discord-py
  # do the long inefficient loop through every channel but set the limit to 10 and it should get them
  # i think
  # print(message.author.history(limit = 10))
  # okay that doesn't send what i need it sends <async_generator object Messageable.history at 0x000002A4FCDEAF40>

with open("token", "r+") as keyfile:
    key = keyfile.read()
    client.run(key)