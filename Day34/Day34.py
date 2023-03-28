import os, time
Emails= []

def printEmail():
    print()
    for item in Emails:
        print(item)
    print()
    
def addEmail():
    item = input("Email: ")
    Emails.append(item)
    time.sleep(1)
    os.system("clear")
        
def removeEmail():
    item = input("Email to remove: ")
    if item in Emails:
        Emails.remove(item)
    else:
        print("Email does not exist")

def viewEmail():
    count= 1
    time.sleep(1)
    os.system("clear")
    print("List of emails")
    for item in Emails:
        print(count, ". ", item)
        count+= 1
    time.sleep(3)
    os.system("clear")

def spam():
    time.sleep(1)
    os.system("clear")
    print("Time to get crazy")
    for item in Emails:
        message= ["Congratulations! You've won a $1000 giftcard. Go to https://join.replit.com/python to claim it now",
         "Your IRS tax refund is pending acceptance. Must accept within 24hrs: https://join.replit.com/python",
          "Amazon is sending you a refund of $35.64. Please reply with your bank account and routing number to receive your refund",
           "Standard Chartered Bank: Your account is temporarily locked. Please log in at https://join.replit.com/python to secure your account",
            "Hello, your FEDEX package with tracking code DZ-6287-FY35 is waiting for you to set delivery preference: https://join.replit.com/python",
             "Apple notification: Your Apple iCloud ID expires today. Login to prevent deletion https://join.replit.com/python",
              "Thank you for your recent Amazon purchase, you've been charged $108.67. If there has been a mistake, okease call (407) 572-7720."]
        import random
        spamRandom = random.randint(0, 6)
        print(f"{item}\n{message[spamRandom]:>40}")
        print()
    

while True:
    operation= input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n>>> ")
    if operation == "1":
        addEmail()
    elif operation == "2":
        removeEmail()
    elif operation == "3":
         viewEmail()
    elif operation == "4":
         spam()
         break
