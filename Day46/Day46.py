import random, time, os
avatar = {}

def compiler():
    print()
    for key, value in avatar.items():
        print(key, end=": ")
        for subKey, subValue in value.items():
            print(subKey, subValue)
        print()
            

playAgain= "yes"
while playAgain == "yes" or playAgain =="y":
    name= input("Avatar's name: ").capitalize()
    type= input("What type of avatar(earth, water, air or fire): ").capitalize()
    specialMove= input("What can your avatar do? ").capitalize()
    startingHP = ((random.randint(1,8))*(random.randint(1,6))+ 10)/2
    startingMP= ((random.randint(1,8))*(random.randint(1,6))+12)/2

    avatar[name] = {"\nSkill: ": specialMove, "HP: ": startingHP, "MP: ": startingMP}
    compiler()
    playAgain= input("Play again?(yes or no): ").lower()
