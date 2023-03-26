import random
val= random.randint(1,100)
trial = 0
while trial < 8:
    guess = int(input("I'm thinking of a number between 1 and 10. Take a guess: "))
    if guess < val and trial < 8:
        print("Your number is too low. Try again")
        trial += 1
    if guess > val and trial < 8:
        print("Your value is too high. Try again")
        trial += 1
    
    if guess == val:
        print("Correct")
        trial += 1
        print ("You got it in " + str(trial) + " trials")
        break
    if trial == 8 and guess != val:
        print("Game over. You missed all 8 trials")
