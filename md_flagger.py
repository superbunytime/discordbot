def md_flagger(str):
	lb, rb, lp, rp = "[", "]", "(", ")"
	lbi, rbi, lpi, rpi = str.find(lb), str.find(rb), str.find(lp), str.find(rp)
	if lb in str and rbi > lbi and lp in str and rpi > lpi:
		return True
	else:
		return False

		# this works

	# if lb in str and rb in str[lbi:-1]:
	# 	# print(f"{str} has []")
		
	# 	if lp in str[rbi:-1] and rp in str[lpi:-1]:
	# 		# print(f"{str} has []()")
	# 		return True

	# else:
	# 	# print(f"{str} does not have []()")
	# 	return False

		# this doesn't work

"""tests"""

# str1 = "[]()"
# str2 = "nope"
# str3 = "[])("
# str4 = "[www.twitch.tv/sussybnuuy](https://www.twitch.tv/puppypotion)" # moment of truth

# print(md_flagger(str1))
# print(md_flagger(str2))
# print(md_flagger(str3))
# print(md_flagger(str4))

"""notes"""

# tests all work, now it needs to be properly integrated into the bot
# and the delete/pk handling needs to be done
# that's done, unless the message needs to be manually deleted; for now it just warns.