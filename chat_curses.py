import random

curses_list = ["end every message with 'uwu'", "type with your nose (no backspace)", "type without using vowels", "speak in emoji only", "type in reverse", "only speak in haiku","-2% butt fat"]

duration_list = [3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 60]

def rand(list):
    return random.choice(list)

def curse_generator():
    curse = rand(curses_list)
    dur = rand(duration_list)
    return (f"you have been cursed to {curse} for {dur} minutes!")