import random
def randomInt():
    return random.randint(10,90)
    
bingo = [[randomInt(), randomInt(), randomInt()],
               [randomInt(), "BINGO", randomInt()],
               [randomInt(), randomInt(), randomInt()]]
print(bingo[0][0], end="      |      ")
print(bingo[0][1], end="      |     ")
print(bingo[0][2])
print(bingo[1][0], end="      |   ")
print(bingo[1][1], end="   |     ")
print(bingo[1][2])
print(bingo[2][0], end="      |      ")
print(bingo[2][1], end="      |     ")
print(bingo[2][2])
