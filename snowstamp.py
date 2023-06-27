import datetime

"""At the start of my project, I had overlooked a discord method that would get a timestamp for me.
Due to this, I spent a week reverse engineering the timestamps of messages sent by extracting it from the message ID and bit shifting it.
While this code is no longer necessary, it took a lot of work, and I want to showcase that I solved a unique problem, even if it was of my own making."""

DISCORD_EPOCH = 1420070400000

def snowFlakeMilli(num):
      """Insert snowflake here to convert to milliseconds; this destroys the snowflake :("""
      return round(num * 1000)

def timeExtractor(snowflake, epoch = DISCORD_EPOCH):
	"""get the bitshifted millisecond value; a long number that's not very human readable."""
	milliseconds = snowFlakeMilli((snowflake >> 22) + epoch)
	print(milliseconds)
	return milliseconds

def createTimestamp(snowflake):
	"""convert long number to actual timestamp! Yay!! the snowflake's destruction was not in vain."""
	shaveMe = timeExtractor(snowflake)/1000000 #shaving off the right amount of digits
	timestamp = datetime.datetime.fromtimestamp(shaveMe).ctime() #converting to timestamp
	return timestamp