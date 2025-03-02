import random

tarot_list = ["0 - The Fool", "I - The Magician", "II - The High Priestess", "III - The Empress", "IV - The Emperor", "V - The Hierophant", "VI - The Lovers", "VII - The Chariot", "VIII - Strength", "IX - The Hermit", "X - The Wheel of Fortune", "XI - Justice", "XII - The Hanged Man", "XIII - Death", "XIV - Temperance", "XV - The Devil", "XVI - The Tower", "XVII - The Star", "XVIII - The Moon", " XIX - The Sun", "XX - Judgment", "XXI - The World", "Ace of Wands", "2 of Wands", "3 of Wands", "4 of Wands", "5 of Wands", "6 of Wands", "7 of Wands", "8 of Wands", "9 of Wands", "10 of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands", "Ace of Pentacles", "2 of Pentacles", "3 of Pentacles", "4 of Pentacles", "5 of Pentacles", "6 of Pentacles", "7 of Pentacles", "8 of Pentacles", "9 of Pentacles", "10 of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles", "Ace of Swords", "2 of Swords", "3 of Swords", "4 of Swords", "5 of Swords", "6 of Swords", "7 of Swords", "8 of Swords", "9 of Swords", "10 of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Cups", "2 of Cups", "3 of Cups", "4 of Cups", "5 of Cups", "6 of Cups", "7 of Cups", "8 of Cups", "9 of Cups", "10 of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups"]

invert_bool =["", " [inverted]"]

proxy_list = list(range(0, 77))

def rand(list):
    return random.choice(list)

# def tarot_generator():
#     tarot = rand(tarot_list)
#     inv = rand(invert_bool)
#     return (f"your card is {tarot}{inv}")

#print(tarot_generator())

top = 0
bottom = -1
middle = 48
# constants for drawing positions
draw_point = top
# default drawing position if not defined

def tarot_generator(num, draw_point, deck_position_text):
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

# print(tarot_generator(9, top, "top"))