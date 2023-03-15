import time,os,random
order= []

def addOrder():
    print()
    name= input("Name: ")
    try:
        number= int(input("How many pizza(s): "))
    except:
        print("Enter a numeric value")
        number= int(input("How many pizza(s): "))
    size= input("What size?(small, medium, large, extra large): ")
    price= (random.randint(1, 10))*number
    set= [name, number, size, price]
    order.append(set)
    print(f"Alright {name}. That would cost {price}. We'll have your order ready in a bit.")
    try:
        f = open("pizza.ppt", "a")
        delist= ''.join(str(order))
        f.write(delist+ "\n")
        f.close()
    except:
        print("File doesn't exist")
    time.sleep(2.8)
    os.system("clear")


def viewOrder():
    time.sleep(1)
    os.system("clear")
    option= input("1. See orders history\n2. See current orders\n>>")
    time.sleep(1)
    os.system("clear")
    if option == "1":
        print("Previous orders")
        f= open("pizza.ppt", "r")
        stuff = "".join(f.read())
        f.close()
        print((stuff))
        
    if option == "2":
        print("Recent orders")
        for row in order:
            for item in row:
                print(item, end= " / ")
            print()
        print()
    time.sleep(2.3)
    os.system("clear")


while True:
    operation= input("Welcome to Pizza King.\n1. Place an order\n2. View Orders\n3. Exit\n>>>")
    if operation == "1":
        addOrder()
    if operation == "2":
        viewOrder()
    if operation == "3":
        print("Closed")
        exit()
    if operation != "1" and operation != "2" and operation != "3":
        print("Invalid operation")
        break
  