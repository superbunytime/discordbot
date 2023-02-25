import datetime

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