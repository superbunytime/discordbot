import random
import array

"""TODO
nothing it's perfect"""

tarot_list = ["the tail","the bowl","the cone","the cat","the interloper","the collar","the leash","gemini stranger","the smell","the clicker","the flavor","the vet","the pound","the bath","the howl","the bark","the cage","the plushie","the hose","the bone","the park","the car","the muzzle","the hydrant", "the owner","the balloon dog", "ace of balls", "2 of balls", "3 of balls", "4 of balls", "5 of balls", "maw of balls", "snout of balls", "ear of balls", "eye of balls", "puppy of balls", "seeker of balls", "guardian of balls", "jewel of balls", "sparkledog of balls", "ace of treats", "2 of treats", "3 of treats", "4 of treats", "5 of treats", "maw of treats", "snout of treats", "ear of treats", "eye of treats", "puppy of treats", "seeker of treats", "guardian of treats", "jewel of treats", "sparkledog of treats", "ace of pets", "2 of pets", "3 of pets", "4 of pets", "5 of pets", "maw of pets", "snout of pets", "ear of pets", "eye of pets",  "puppy of pets", "seeker of pets", "guardian of pets", "jewel of pets", "sparkledog of pets", "ace of fangs", "2 of fangs", "3 of fangs", "4 of fangs", "5 of fangs", "maw of fangs", "snout of fangs", "ear of fangs", "eye of fangs","puppy of fangs", "seeker of fangs", "guardian of fangs", "jewel of fangs", "sparkledog of fangs", "ace of fleas", "2 of fleas", "3 of fleas", "4 of fleas", "5 of fleas", "maw of fleas", "snout of fleas", "ear of fleas", "eye of fleas", "puppy of fleas", "seeker of fleas", "guardian of fleas", "jewel of fleas", "sparkledog of fleas"]

invert_bool =["", " [inverted]"]

proxy_list = list(range(0, 95))

def rand(list):
    return random.choice(list)

top = 0
bottom = -1
middle = 48
# constants for drawing positions
draw_point = top
# default drawing position if not defined

def barkana_generator(num, draw_point, deck_position_text):
    if num == "":
       num = 1
    proxy_pulls = []
    pulls = []
    random.shuffle(proxy_list)
    i = 0
    while i < num:
        # remove an item from the array at the deck position (top, middle, bottom)
        proxy_pulls.append(proxy_list[draw_point])
        proxy_list.remove(proxy_list[draw_point])
        i += 1
    i = 0
    while i < num:
       inv = rand(invert_bool)
       # append the corresponding card from the barkana list to its own array
       pulls.append(f"{tarot_list[proxy_pulls[i]]}{inv} ")
       i += 1
    for x in proxy_pulls:
       proxy_list.append(proxy_pulls[0])
       proxy_pulls.remove(proxy_pulls[0])
    # re-incorporate the drawn numbers back into the array (at the end)
    random.shuffle(proxy_list)
    # shuffle the deck
    your_hand = ""
    if len(pulls) > 1:
      i = 0
      while i < len(pulls):
        your_hand += pulls[i]
        your_hand += "\n"
        i += 1
      print(f"this is the draw_point: {draw_point}")
      return f"drawing from the {deck_position_text} of the deck... your cards are \n{your_hand}"
    else:
      your_hand += pulls[0]
      print(f" this is the draw_point:{draw_point}")
      return f"drawing from the {deck_position_text} of the deck... your card is \n{your_hand}"
    # return the string of cards chosen.

# print(barkana_generator(9, top, "top"))