from replit import db
import os, time, datetime

def addItems():
    entry= input("\nWhat's on your mind\n>>>")
    timestamp = datetime.datetime.now()
    key = f"txt{timestamp}"
    db[key] = entry
    time.sleep(1)
    os.system("clear")


def viewItems():
    matches = db.prefix("txt")
    matches = matches[::-1]
    for i in matches:
        print()
        print(db[i])
   # print()
        time.sleep(0.3)
    time.sleep(1)
    os.system("clear")



def menu():
    operation = input("Welcome to your secure diary\n1. Write in your diary\n2. View entries\n>>>")
    if operation == "1":
        addItems()
    if operation == "2":
        viewItems()

password= "Sandee563#"
key = "pass"
db[key] = password

access= input("Password: ")
if access == password:
    time.sleep(0.5)
    os.system("clear")
    while True:
        menu()
else:
    print("Invalid password")

