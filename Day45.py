import time, os
todo= []

def addItems():
    name= input("\nName of task\n>>")
    dueDate= input("Date for task to be due\n>>")
    priority= input("Priority(High, Medium or low)\n>>").lower()
    set= [name, priority, dueDate]
    todo.append(set)
    time.sleep(0.5)
    print("Added")
    time.sleep(0.9)
    os.system("clear")


def removeItems():
    time.sleep(1)
    os.system("clear")
    cancel = input("What task do you want to remove? ")
    for row in todo:
        if cancel in row:
            todo.remove(row)
            time.sleep(0.5)
            print("Removed")
    if cancel not in row:
        print("That task doesn't exist")
    time.sleep(1)
    os.system("clear")
        

def viewItems():
    time.sleep(1)
    os.system("clear")
    options= input("1. View all\n2. View by priority\n>>")
    time.sleep(0.7)
    os.system("clear")
    if options == "1":
        for row in todo:
            for item in row:
                print(item, end= " / ")
            print()
        print()
        time.sleep(1.6)
    if options == "2":
        priority = input("What priority? > ")
        for row in todo:
            if priority in row:
                for item in row:
                    print(item, end=" / ")
                print()
            print()
            time.sleep(1.5)
        if priority not in row:
            print("No tasks with that priority")
            time.sleep(1)
    else:
      print("Invalid option")
    os.system("clear")


def updateItems():
    time.sleep(1)
    os.system("clear")
    print("Which tasks have been completed?\nAll completed tasks will be deleted")
    complete= input("Task name\n>>")
    for row in todo:
        if complete in row:
            todo.remove(row)
            time.sleep(0.5)
            print("Nice job")
    if complete not in row:
        print("That task doesn't exist in task list")
    time.sleep(1)
    os.system("clear")
    
    
while True:
    operation = input("Welcome to your todo menu. What do you want to do?\n1. Add task\n2. Remove task\n3. View tasks\n4. Update on a task\n>>>")
    if operation == "1":
        addItems()
    if operation == "2":
        removeItems()
    if operation == "3":
        viewItems()
    if operation == "4":
        updateItems()
    
