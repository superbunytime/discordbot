import random


def d(n):
  num = (random.randrange(1, n + 1))
  if n == 20:
    if num == 1:
      return "1... oof."
    if num == 20:
      return "20!  Critical!!"
    else:
      return num
  return num

# print(d(621))