import random


def d20():
  num = (random.randrange(1,21))
  if num == 1:
    return "1... oof."
  if num == 20:
    return "20!  Critical!!"
  else:
    return num

#print(d20())