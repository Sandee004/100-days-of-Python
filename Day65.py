import random
names= ["Boris", "Rishi", "Mike", "Roshan", "Bill", "Ted", "Station"]
time = ["Day", "Night"]

class Character():
    name = None
    health = None
    points = None
    def __init__(self, name, health, points):
        self.name = name
        self.health = health
        self.points = points

class Player(Character):
    def __init__(self, lives, alive):
        self.name= "David"
        self.health = random.randint(1,10)*15
        self.points = random.randint(1,10)*10
        self.lives = lives
        self.alive = alive
        
class Vamp(Character):
    def __init__(self, type, strength, period):
        self.name = random.choice(names)
        self.health = random.randint(1,10)*15
        self.points = random.randint(1,10)*10
        self.type = type
        self.strength = strength
        self.period = period
        
class Vamp2(Character):
    def __init__(self, type, strength, period):
        self.name = random.choice(names)
        self.health = random.randint(1,10)*15
        self.points = random.randint(1,10)*10
        self.type = type
        self.strength = strength
        self.period = period

class Orc(Character):
    def __init__(self, type, strength, speed):
        self.name = random.choice(names)
        self.health = random.randint(1,10)*15
        self.points = random.randint(1,10)*10
        self.type = type
        self.strength = strength
        self.speed = speed
    

char1 = Player("3", "Yes")
print(f"Name: {char1.name}\nHealth: {char1.health}\nMagic points: {char1.points}\nLives: {char1.lives}\nAlive: {char1.alive}")
print()

char2 = Vamp("Vampire", f"{random.randint(1,10)*12}", f"{random.choice(time)}")
print(f"Name: {char2.name}\nHealth: {char2.health}\nMagic points: {char2.points}\nType: {char2.type}\nStrength: {char2.strength}\nDay/Night: {char2.period}")
print()

char3 = Vamp2("Vampire", f"{random.randint(1,10)*12}", f"{random.choice(time)}")
print(f"Name: {char3.name}\nHealth: {char3.health}\nMagic points: {char3.points}\nType: {char3.type}\nStrength: {char3.strength}\nDay/Night: {char3.period}")
print()

char4 = Orc("Orc", f"{random.randint(1,10)*12}", f"{random.randint(1, 30)}")
print(f"Name: {char4.name}\nHealth: {char4.health}\nMagic points: {char4.points}\nType: {char4.type}\nStrength: {char4.strength}\nSpeed: {char4.speed}")
print()

char5 = Orc("Orc", f"{random.randint(1,10)*12}", f"{random.randint(1, 30)}")
print(f"Name: {char5.name}\nHealth: {char5.health}\nMagic points: {char5.points}\nType: {char5.type}\nStrength: {char5.strength}\nSpeed: {char5.speed}")
print()

char6 = Orc("Orc", f"{random.randint(1,10)*12}", f"{random.randint(1, 30)}")
print(f"Name: {char6.name}\nHealth: {char6.health}\nMagic points: {char6.points}\nType: {char6.type}\nStrength: {char6.strength}\nSpeed: {char6.speed}")
print()

