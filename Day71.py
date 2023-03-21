import os, time, random
from replit import db

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  
  db[username] = {"password": newPassword, "salt": salt}
  print("User added")
  print()

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    time.sleep(0.7)
    os.system("clear")
    return
  

  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]!=newPassword:
    print("Username or password incorrect")
    print()
    time.sleep(1)
    os.clear
  elif db[username]["password"]==newPassword:
    time.sleep(1)
    os.system("clear")
    print("Log in successful. Holla")
    exit()
      


while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])