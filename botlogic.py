"""this is for the channel role management logic for sussy's self promo channel
   this current version will be for testing in my own bot test server until it works"""

"""TO DO
query a user for the number of messages sent within the last 7 days (168 hours, 10,080 minutes, 604,800 seconds); log the number of messages for debug purposes.
if message_threshold >= 5 and role ! exist on user, append role to user; if < 5 and role exist on user, remove role from user
once that works on the user level, loop through every user on the server and run the logic on them to determine if the role is to be appended or removed.  Once you can loop through every user, have the bot automatically perform this at a set intreval."""

"""Notes: audit_log is not the command i need.  print(message.author.id) is what worked for getting the author id.  Now it just needs to be saved to a python object and incremented on each message.  Pog.

it may be inefficient to store the entirety of the active userbase as a single object, but it will do in a pinch.

So a potential issue while contemplating the data structure design is that at relaunch the count variables are destroyed and reset to the base value, which means every time it's relaunched, the bot will wind up wiping the role from otherwise qualified users.  A simple(er) workaround would be JSONifying the object i guess."""

MESSAGE_THRESHOLD = 5
ROLLING_WINDOW = 7

class dUser:
   def __init__(self, id, msgCount):
      self.id = id
      self.msgCount = msgCount

cinnabun = dUser(257032548431953922, 0)
