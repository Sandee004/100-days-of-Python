import random
def rollDice(sides):
  result = random.randint(1,sides)
  return result
  
def Dice():
    import random
    value1 = random.randint(1,6)
    value2 = random.randint(1,8)
    health = value1 * value2
    return (health)
    
haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(Dice())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")
