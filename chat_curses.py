import random

curses_list = ["end every message with 'uwu'", "type with your nose (no backspace)", "type without using vowels", "speak in emoji only", "type in reverse", "roleplay as a random fursona (use random fursona generator command)", "only speak in haiku"]

duration_list = [3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 60]

def rand(list):
    return random.choice(list)

def curse_generator():
    curse = rand(curses_list)
    dur = rand(duration_list)
    return (f"you have been cursed to {curse} for {dur} minutes!")

print(curse_generator())