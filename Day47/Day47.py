import os, time, random
trumps = {}
def randomizer():
    value= random.randint(1, 250)
    return value
randoms= randomizer()

trumps["David"] = {"Intelligence": randoms, "Speed": randoms, "Guile": randoms, "Baldness Level": randoms}
trumps["Mr Spock"] = {"Intelligence": randoms, "Speed": randoms, "Guile": randoms, "Baldness Level": randoms}
trumps["Monica"] = {"Intelligence": randoms, "Speed": randoms, "Guile": randoms, "Baldness Level": randoms}
trumps["Professor X"] = {"Intelligence": randoms, "Speed": 1, "Guile": randoms, "Baldness Level": randoms}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  for key in trumps:
      print(key)
  user = input("Pick your character\n> ").capitalize()
  if user not in trumps.keys():
      print("Invalid character choice")
      break
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ").capitalize()

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")


  time.sleep(2.5)
  os.system("clear")
