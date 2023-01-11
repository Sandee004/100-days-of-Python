print("So I'm gonna be helping with quadratic equations today. Enter the three parameters...")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

positive = round(((-1*b) + (b**2 - 4*a*c)**0.5)/(2*a), 3)
negative = round(((-1*b) - (b**2 - 4*a*c)**0.5)/(2*a), 3)
print("Two values are ", positive, "and", negative)