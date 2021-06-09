
"""
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

while True:
    player1 = input("Player1: Enter 1 for Rock, 2 for Paper, 3 Scissors: ")
    player2 = input("Player2: Enter 1 for Rock, 2 for Paper, 3 Scissors: ")
    if (player1 == "1" and player2 == "1") or (player1 == "2" and player2 == "2") or (player1 == "3" and player2 == "3"):
        print("we chose the same thing!")
    elif (player1 == "1" and player2 == "2") or (player1 == "2" and player2 == "3") or (player1 == "3" and player2 == "1"):
        print("Congratulation Player2 You Wins!")
    elif (player1 == "1" and player2 == "3") or (player1 == "3" and player2 == "2") or ( player1 == "2" and player2 == "1"):
        print("Congratulation Player1 You Wins!")

    rejouer = input("Press 1 to play again and 0 to exit the game? ")
    if rejouer == '0':
        print("See you next time!")
        break