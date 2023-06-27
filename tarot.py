import random

tarot_list = ["0 - The Fool", "I - The Magician", "II - The High Priestess", "III - The Empress", "IV - The Emperor", "V - The Hierophant", "VI - The Lovers", "VII - The Chariot", "VIII - Strength", "IX - The Hermit", "X - The Wheel of Fortune", "XI - Justice", "XII - The Hanged Man", "XIII - Death", "XIV - Temperance", "XV - The Devil", "XVI - The Tower", "XVII - The Star", "XVIII - The Moon", " XIX - The Sun", "XX - Judgment", "XXI - The World", "Ace of Wands", "2 of Wands", "3 of Wands", "4 of Wands", "5 of Wands", "6 of Wands", "7 of Wands", "8 of Wands", "9 of Wands", "10 of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands", "Ace of Pentacles", "2 of Pentacles", "3 of Pentacles", "4 of Pentacles", "5 of Pentacles", "6 of Pentacles", "7 of Pentacles", "8 of Pentacles", "9 of Pentacles", "10 of Pentacles", "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles", "Ace of Swords", "2 of Swords", "3 of Swords", "4 of Swords", "5 of Swords", "6 of Swords", "7 of Swords", "8 of Swords", "9 of Swords", "10 of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords", "Ace of Cups", "2 of Cups", "3 of Cups", "4 of Cups", "5 of Cups", "6 of Cups", "7 of Cups", "8 of Cups", "9 of Cups", "10 of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups"]

invert_bool =["", " [inverted]"]

def rand(list):
    return random.choice(list)

def tarot_generator():
    tarot = rand(tarot_list)
    inv = rand(invert_bool)
    return (f"your card is {tarot}{inv}")

#print(tarot_generator())