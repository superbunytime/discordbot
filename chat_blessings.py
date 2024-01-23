import random

def rand(list):
    return random.choice(list)

good_effects =[ "pog", "cry-laughing", "awe", "dumbfoundedness", "relaxation", "soothe", "cute-aggression", "laughter"]

duration_list = [3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 10, 20, 60]

blessings_list = ["good luck in conversation", "easier access to flow state", "critical success on your next crafting roll","enhanced power level detection","the 'detect wood quality' buff","increased likelihood of leaving a good first impression","flirting skills up","+20% magic find for 30 minutes","increased moisture duration","+0.5% size","an inventory UI that's shaped a little bit more like a smiley face","more","your phone being in the first pocket you check","you might see a bird","You should try hugging someone","+10% to perception checks relating to zenzi","you can now sense rabbits within a 50 foot radius","a mental image of a cute rabbit","5% increase to gay","+1 pronoun slot (empty)"," 100 rats now follow your command...somewhere!","+0.1% soul attunement (permanent, stacking)", "+2% butt fat","+1% damage with axe class weapons","you can remember 1 more sequential number",f"+{rand(list(range(1, 101)))}% chance of inflicting {rand(good_effects)}"]

def bless_generator():
    # takes a list argument for appending the username, bless, and duration to
    # list will look something like this:
    # dict_list = []
    # taking a break to implement what we have now
    bless = rand(blessings_list)
    dur = rand(duration_list)
    # return (f"you have been blessed with {bless} for {dur} minutes!")
    return [bless, dur]