print("Building your starwars profile")
first= input("Firstname: ").capitalize()
last= input("Last name(surname): ").lower()

firstPrt= first[:3]
secondPrt= last[:3]
firstName= (f"{firstPrt}{secondPrt}")

maiden= input("Enter your mum's maiden name: ").capitalize()
city= input("State of Birth: ").lower()

maidenSlice= maiden[:2]
citySlice= city[:-3]
lastName= (f"{maidenSlice}{citySlice}")
print()
print(f"Starwars name: {firstName} {lastName}")
