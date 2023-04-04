import random


def d20():
  num = (random.randrange(1,21))
  if num == 1:
    return "1... oof."
  if num == 20:
    return "20!  Critical!!"
  else:
    return num

def d12():
  num = (random.randrange(1,13))
  return num

def d10():
  num = (random.randrange(1,11))
  return num

def d8():
  num = (random.randrange(1,9))
  return num

def d6():
  num = (random.randrange(1,7))
  return num

def d4():
  num = (random.randrange(1,5))
  return num
def d100():
  num = (random.randrange(1,101))
  return num