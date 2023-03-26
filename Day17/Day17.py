import emoji
from getpass import getpass as input
print("We're gonna be playing a simple Rock Paper Scissors game today. R means Rock, P means Paper and S means Scissors")


player1_score= 0
player2_score= 0
while (player1_score or player2_score)< 2:
    player1= input("Player 1 ( R, P or S): ").upper()
    player2= input("Player 2(R, P or S): ").upper()

    if (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (player1 == "S" and player2 == "P"):
        player1_score += 1
        print("Player 1 score= " + str(player1_score))
        print("Player 2 score= " + str(player2_score))

    if (player1 == "R" and player2 == "P") or (player1 == "P" and player2 == "S") or (player1 == "S" and player2 == "R"):
        player2_score += 1
        print("Player 1 score= " + str(player1_score))
        print("Player 2 score= " + str(player2_score))
    
    if (player1 == "R" and player2 == "R") or (player1 == "P" and player2 == "P") or (player1 == "S" and player2 == "S"):
        print(emoji.emojize("It's a tie :face_with_tongue:"))

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "q", "t", "u", "v", "w", "x", "y", "z"]
    if (player1.lower() in letters) or (player2.lower() in letters):
        print(emoji.emojize("Invalid input detected :cross_mark:"))
        
    if player1_score == 2:
        print(emoji.emojize("Player 1 wins :party_popper:"))
    if player2_score == 2:
        print(emoji.emojize("Player 2 wins :party_popper:"))
