import random
name= input("Avatar's name: ").capitalize()
type= input("What type of avatar(earth, water, air or fire): ").capitalize()
specialMove= input("What can your avatar do? ").capitalize()
startingHP = ((random.randint(1,8))*(random.randint(1,6))+ 10)/2
startingMP= ((random.randint(1,8))*(random.randint(1,6))+12)/2

details= {"Name": name, "Type": type, "Skill": specialMove, "HP": startingHP, "MP": startingMP}
print("\nAvatar Details")
for name,value in details.items():
      if details["Type"]== "Fire":
          print(f"\033[31m {name}: {value}")
      elif details["Type"] == "Water":
          print(f"\033[34m {name}: {value}")
      elif details["Type"] == "Earth":
          print(f"\033[0;33m {name}: {value}")
      elif details["Type"] == "Air":
          print(f"\033[0m {name}: {value}")
      else:
          print("Pick a valid avatar type")