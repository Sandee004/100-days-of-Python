import random
ask= int(input("Number of sides of dice: "))
playAgain = "yes"

def dice(ask):
    value= random.randint(1, ask)
    print("You rolled a " + str(value))
while playAgain == "yes":
    dice(ask)
    playAgain = input("Roll again?")
