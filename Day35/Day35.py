import time, os
myAgenda = []

def printList():
    count= 1
    time.sleep(1)
    os.system("clear")
    print("Pending tasks")
    for item in myAgenda:
        print(f"{count}. {item}")
        count+= 1
    time.sleep(3)
    os.system("clear")

def addItem():
        item = input("What task do you want to add? ")
        if item not in myAgenda:
             myAgenda.append(item)
        else:
             print("Task already exists")
        time.sleep(1)
        os.system("clear")

def removeItem():
    item = input("What task do you want to remove? ")
    if item in myAgenda:
        confirmation = input("Are you sure you want to delete this task?").lower()
        if confirmation == "yes":
            myAgenda.remove(item)
        else:
            print("Aborted")
            time.sleep(1)
            os.system("clear")
    else:
        print("Doesn't exist in list of tasks")
        
        
while True:
    operation= input("Choose an operation\n1. Add items \n2. Remove items \n3. View tasks \n4. Clear all tasks \n>>>")
    if operation == "1":
        addItem()
    elif operation == "2":
        removeItem()
    elif operation == "3":
        printList()
    elif operation == "4":
        myAgenda.clear()
        print("Cleared")
        time.sleep(1)
        os.system("clear")
    else:
        print("That operation is not recognized")
