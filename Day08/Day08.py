print('Pydroid today is gonna be your motivator ;)')
name = input("What's the name Champ? ")
day = input("What day of the week is it? Type in full: ").lower()

if day == "monday":
  print("It's a wonderful new week with amazing oppurtunities. Let's go get it!!")
  
elif day == "tuesday":
  print("How are your plans for the week going", name, ". I'm rooting for your success")
  
elif day == "wednesday":
  print("You're halfway through. How are things coming along? You can do it")
  
elif day == "thursday":
  print("Breatheeee.....3 days more. Blow off some steam and move. Weekend is almost here.")
  
elif day == "friday":
  print("Friyay!!! You made it. Round off your tasks for the week and plan a wonderful and restful weekend")
  
elif day == "saturday" or day == "sunday":
  print("Leisure dayy")
  
else:
  print("Is that the name of a day", name, "?")
