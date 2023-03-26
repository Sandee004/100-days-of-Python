import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("Guess my number. It's between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations! That's right!")
        break
    else:
        print("Err.....try again!")
