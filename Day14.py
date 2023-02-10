import emoji
from getpass import getpass as input
print("We're gonna be playing a simple Rock Paper Scissors game today. R means Rock, P means Paper and S means Scissors")
player1= input("Player 1 ( R, P or S): ").upper()
player2= input("Player 2(R, P or S): ").upper()
if (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (player1 == "S" and player2 == "P"):
    print(emoji.emojize("Player 1 wins :party_popper:"))

if (player1 == "R" and player2 == "P") or (player1 == "P" and player2 == "S") or (player1 == "S" and player2 == "R"):
    print(emoji.emojize("Player 2 wins :party_popper:"))
    
if (player1 == "R" and player2 == "R") or (player1 == "P" and player2 == "P") or (player1 == "S" and player2 == "S"):
    print(emoji.emojize("It's a tie :face_with_tongue:"))

else:
    print(emoji.emojize("Invalid input detected :cross_mark:"))