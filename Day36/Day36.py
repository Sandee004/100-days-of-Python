name= []

def nameList():
    for item in name:
        print(item)
    print()

def addName():
        first = input("First Name: ").capitalize().strip()
        last= input("Last name(surname): ").capitalize().strip()
        item = (f"{first} {last}")
        if item not in name:
            name.append(item)
            print()
            print("List of names")
            nameList()
        else:
            print("Name already exists")
            print()

while True:
    addName()
