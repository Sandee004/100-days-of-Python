print("Welcome to Character Builder")
def healthStat():
    import random
    value1 = random.randint(1,6)
    value2 = random.randint(1,12)
    health = (((value1 * value2)/2) +10)
    return str(health)

def strengthStat():
    import random
    value1 = random.randint(1,6)
    value2 = random.randint(1,12)
    strength = (((value1 * value2)/2) +12)
    return str(strength)

Character = "yes"
while Character == "yes":
    name= input("Name your character: ")
    characterType = input("Character type (Vampire, Warewolf, Other): ")
    print("HEALTH: " + healthStat())
    print("STRENGTH: " + strengthStat())
    print()
    Character = input("Build another character? ").lower
