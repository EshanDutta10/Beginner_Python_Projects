import random


def play():

    print("ROCK PAPER SCISSORS GAME \n1.Press 'r' for Rock\n2.Press 'p' for Paper\n3.Press 's' for Scissors.\n")
    user = input("Enter your choice: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a Tie!"
    elif win(user,computer):
        return "You Win!"
    else:
        return "You Lost!"


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


choice = 'y'
while choice == 'y':
    print(play())
    choice = input("Do you want to play again? y/n: ").lower()
    print("\n")
