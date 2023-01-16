import bot
"""this is for the channel role management logic for sussy's self promo channel
   this current version will be for testing in my own bot test server until it works"""

"""TO DO
on start, generate a set of all user ids in the server
add any new users to the database
query the amount of messages sent within the last 7 days to determine roles
append or remove role (or if no changes, do nothing) from each user respectively on database
pull database status of role and apply to actual role
rest for 12 hours and repeat the process.
"""

MESSAGE_THRESHOLD = 5
ROLLING_WINDOW = 7 #days

class dUser:
   def __init__(self, id, msgCount):
      self.id = id
      self.msgCount = msgCount

cinnabun = dUser(257032548431953922, 0) #initialize message count with 0

def member_list(set):
    for member in bot.client.get_all_members():
      set.add(member)

set1 = set()
# member_list(set1)
# print(set1)
