import datetime, time, os
from replit import db

def addTweet():
    tweet= input("\nTweet\n>>>")
    timestamp = datetime.datetime.now()
    key = f"mes{timestamp}"
    db[key] = tweet
    time.sleep(1)
    os.system("clear")
    

def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print()
    print(db[i])
   # print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      more = input("Next 10?: ")
      if(more.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")

    
while True:
    operation= input("Welcome to main menu\n1. Add Tweet\n2. View Tweets\n>>>")
    if operation == "1":
        addTweet()
    if operation == "2":
        viewTweet()


