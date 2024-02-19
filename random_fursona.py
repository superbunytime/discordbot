import random

"""
TODO
convert to object oriented paradigm
abstract data (lists) to another file
add items to sample lists
create method to determine which random optional parameters to roll for (rarity color system)
add small weighted chance for special classes, like species fusions, galactic color, rainbow, superpowers, weaknesses
"""

species_list = ["bird", "dog", "bunny", "cat", "avali", "hare", "protogen", "moth", "salamander", "chimera", "bat", "cow", "wolf", "fox", "coyote", "sheep", "goat", "deer", "dragon", "wyvern", "spider", "horse", "lion", "tiger", "bear", "shark",
                "hyena", "bee", "lamia", "kangaroo", "possum", "wombat", "skunk", "slug", "sea slug", "moogle", "ferret", "weasel", "stoat", "otter", "dryad", "raccoon", "alligator", "crocodile", "snake", "rat", "mouse", "chipmunk", "squirrel", "fennec", "kitsune", "puma", "pangolin", "mamagen"]
color_list = ["aqua", "aquamarine", "azure", "beige", "bisque", "black", "blue", "blue violet", "brown", "chartreuse", "chocolate", "coral", "crimson", "cyan", "dark blue", "dark cyan", "dark goldenrod", "dark green", "dark khaki", "dark magenta", "dark olive green", "dark orange", "dark orchid", "dark red", "dark sea green", "dark turquoise", "dark violet", "deep pink", "deep sky blue", "dim gray", "floral white",
              "forest green", "fuchsia", "gold", "goldenrod", "gray", "green yellow", "hot pink", "indigo", "ivory", "khaki", "lavendar", "light blue", "light green", "light sea green", "lime", "magenta", "maroon", "midnight blue", "orange", "orange red", "orchid", "pink", "plum", "powder blue", "purple", "red", "sea green", "sienna", "silver", "sky blue", "teal", "turoquoise", "violet", "white", "yellow", "yellow green", "platinum", "fibromelanotic"]
size_list = ["thimble-sized", "cup full of", "small", "medium", "large", "micro",
             "macro", "subatomic", "galactic", "dumptruck of a", "brick wall of a", "five-dimensional", "dimensionally-inconceivable", "insignificant dust-speck sized"]
ability_list = ["heat vision",
                "non-euclidian geometry", "self-replicating", "extraplanar travel", "ice breath", "intangibility", "ventriloquism", "time stop", "super speed", "microplastic summoning", "identifying wood", "sponge skin", "plushification beam", "bunnification beam", "speedrunning", "trans gendering", "flammable blood", "always inserting usb sticks on the first try", "verbal stimming bun bun bun bun meow meow meow meow", "built in squeaky on contact", "bites you bites you bites you bites you", "you're really good at kissing", "you stink good", "precognition of cats", "gaslighting", "hypnosis", "doing free art", "thoughtfulness", "built-in 5G", "release the bees", "rapid moss growth", "committing felonies", "faster than light bleeding"]
weakness_list = ["an aversion to blenders", "extreme clumsiness",
                 "extreme suggestibility", "a compulsion to shitpost", "a strong desire to play gacha games", "subservience to plushies", "an estrogen addiction", "flammable blood", "spontaneous combustion", "being chased by hungry rats for all time", "witnessing man-made horrors beyond your comprehension", "un plasma'd shrimp", "verbal stimming meow meow meow meow meow", "200 ping irl", "doing free art", "hijacking chat", "being forced to listen to sex tempo music", "only being able to count to 3", "being forced to read chat every time it updates", "anxiety"]
role_list = ["healer", "tank", "mage", "bard", "dps", "support", "alchemist", "knight",
             "deadbeat", "merchant", "diplomat", "rogue", "druid", "necromancer", "nekomancer", "geomancer", "seer", "hardass", "freeloader", "imposter", "crewmate", "idol", "mime", "little pee pee boy", "biochemist"]


def rand(list):
    return random.choice(list)


def fursona_generator():
    species = rand(species_list)
    pcolor, scolor, tcolor = rand(color_list), rand(color_list), rand(color_list)
    size = rand(size_list)
    ability = rand(ability_list)
    weakness = rand(weakness_list)
    role = rand(role_list)
    return (f"you are a {size} {pcolor} {species} with {scolor} highlights. Your special ability is {ability}, and you are cursed with {weakness}. Your party role is {role}")


# print(fursona_generator())
