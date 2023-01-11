def playerBanter():
  if player == "Messi":
    return("Wrong answer. Abeg shift")
  elif player == "Ronaldo":
    return("Legit")
  else:
    return("How dare you!! Abeg shift")

    
football = input("What football club do you support? ").lower()
if football == "manu" or football == "manchester united":
  print("Nice")
  player= input("Who's the G.O.A.T in football? ")
  print(playerBanter())

else:
  print("Meh..")
  player= input("Who's the G.O.A.T in football? ")
  print(playerBanter())