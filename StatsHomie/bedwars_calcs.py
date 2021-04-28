import copy
import math

def xp_per_level (*, level):
    prestige = math.floor (level / 100)
    base = level - (prestige * 100)
    if base >= 5: return 5000
    if base == 4: return 3500
    if base == 3: return 3000
    if base == 2: return 2000
    if base == 1: return 1000
    if base == 0: return 0 if prestige == 0 else 500

def xp_to_level (*, xp):
    level = 0.0
    remaining_xp = copy.copy (xp)
    while True:
        necessary_xp = xp_per_level (level = level)
        if remaining_xp >= necessary_xp:
            level += 1
            remaining_xp -= necessary_xp
        else:
            level += (remaining_xp / necessary_xp)
            break
        if remaining_xp == 0: break
    return level