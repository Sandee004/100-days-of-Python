import os, time, random
print("Idea Storage")
while True:
    option= input("Add new idea or see random idea(a or r): ").lower()
    if option == "a":
        idea= input(">>")
        f = open("test.py", "a+")
        f.write(f">> {idea}\n")
        f.close()
        print("Added")
        time.sleep(1)
        os.system("clear")
        
    if option == "r":
        f = open("test.py", "r")
        ideas = f.read().split("\n")
        f.close
        ideas.remove("")
        idea = random.choice(ideas)
        print(idea)
        time.sleep(1)
        os.system("clear")
        
    else:
        print("Pls input either a or r")