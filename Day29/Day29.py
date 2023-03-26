'''
"\033[?25l" -- ti hide cursor
 '''
def Color(value, word):
  if value=="red":
    print("\033[31m", "\003[3m", word, sep="", end="")
  elif value=="green":
    print("\033[32m",  "\003[3m", word, sep="", end="")
  elif value=="blue":
    print("\033[34m",  "\003[3m", word, sep="", end="")
  elif value=="brown":
        print("\033[0;33m", "\003[3m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("My name is Sandee.")
print("With my ", end="")
Color("red", "new program")
Color("reset", " I can just call red('and') ")
Color("red", "it will print in red ")
Color("blue", "or even blue.")
Color("brown", "Brown works too")
