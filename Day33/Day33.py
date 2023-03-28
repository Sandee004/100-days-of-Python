import time, os
myAgenda = []

def printList():
    print() #this is just to add an extra space between items
    for item in myAgenda:
        print(item)
    print() #this is just to add an extra space between items

def addItem():
        item = input("What task do you want to add? ")
        myAgenda.append(item)
        printList()

def removeItem():
    item = input("What task do you want to remove? ")
    if item in myAgenda:
        myAgenda.remove(item)
        printList()
    else:
        print("Doesn't exist in list of tasks")

def viewItem():
    time.sleep(2)
    os.system("clear")
    printList()

while True:
    operation= input("Do you want to add, remove or view items on your list? ")
    if operation == "add":
        addItem()
    elif operation == "remove":
        removeItem()
    elif operation == "view":
        viewItem()
    else:
        print("That operation is not recognized")
