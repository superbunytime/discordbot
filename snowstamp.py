import datetime

DISCORD_EPOCH = 1420070400000

def snowFlakeMilli(num):
      return round(num * 1000)

def convertSnowflakeToDate(snowflake, epoch = DISCORD_EPOCH):
	milliseconds = snowFlakeMilli((snowflake >> 22) + 1420070400000)
	return milliseconds


def validateSnowflake(snowflake, epoch):

	timestamp = convertSnowflakeToDate(snowflake, epoch)

	return timestamp

def dummy(snowflake):
	goodNumber = convertSnowflakeToDate(snowflake)/1000000
	betterNumber = datetime.datetime.fromtimestamp(goodNumber).ctime()
	return betterNumber