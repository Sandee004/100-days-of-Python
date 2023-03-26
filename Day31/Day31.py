import emoji, os, time
def Color(value, word):
  if value=="red":
    print("\033[31m", word, sep="", end="")
  elif value=="green":
    print("\033[32m", word, sep="", end="")
  elif value=="blue":
    print("\033[34m", word, sep="", end="")
  elif value=="brown":
        print("\033[0;33m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")
    
Color("red", "=")
Color("white", "=")
Color("blue", "=")
Color("brown", "Music App")
Color("blue", "=")
Color("white", "=")
Color("red", "=")
Color("white","\n    🔥▶️   Radio Gaga")
queen = "Queen"
print(f"\n{queen: ^40}")

print()
print()
print()

print("PREV")
next = "NEXT"
nxt= f"{next:^30}"
Color("green", nxt)

pause= "PAUSE"
pse= f"\n{pause:^60} \033[?25l"
Color("red", pse)

time.sleep(3)
os.system("clear")

welcome= "WELCOME TO"
welc= (f"{welcome:^30}")
Color("white", welc)

armbook= "--       ARMBOOK       --"
arm= (f"\n{armbook:^30}")
Color("blue", arm)

rip= "Definitely not a rip off of"
ripOff= (f"{rip:>70}")
Color("brown", ripOff)

certain= "a certain other social"
social= (f"{certain:>56}")
Color("brown", social)

site= "networking site"
networking= (f"{site:>58}")
Color("brown", networking)

print()
print()

honest= "Honest"
honesty= (f"\n{honest:^30}")
Color("red", honesty)

username= "Username: "
user= (f"\n{username:^30}")
Color("white", user)

password= "Password: "
print(f"\n{password:^30} \033[?25l")
