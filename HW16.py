#Name:Ryley Ashcraft
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps_game():
    print("Chose the number 1 for Rock, 2 for Paper, 3 for Scissors")
    playerchoice = int(input())
    opponentchoice = random.randint(1,3)
    if playerchoice == 1 and opponentchoice == 2:
        print("Your opponent chose", opponentchoice)
        print("Opponent beat you with paper")
    elif playerchoice == 1 and opponentchoice == 3:
        print("Your opponent chose", opponentchoice)
        print("You beat your opponent with Rock!")
    elif playerchoice == 2 and  opponentchoice == 1:
        print("Your opponent chose", opponentchoice)
        print("You beat your opponent with Paper")
    elif playerchoice == 2 and opponentchoice == 3:
        print("Your opponent chose", opponentchoice)
        print("Opponent beat you with Scissors")
    elif playerchoice == 3 and opponentchoice == 1:
        print("Your opponent chose", opponentchoice)
        print("Opponent beat you with Rock")
    elif playerchoice == 3 and opponentchoice == 2:
        print("Your opponent chose", opponentchoice)
        print("You beat your opponent with Scissors")
    else:
        print("Invalid Response")
        rps_game()

    if playerchoice == 1 and opponentchoice == 1:
        print("You got a tie!")

    if playerchoice ==2 and opponentchoice == 2:
        print("You got a tie!")

    if playerchoice == 3 and opponentchoice ==3:
        print("You got a tie!")



def replay_rps():
    replaychoice = input("Do you want to play again? Y/N?")
    if replaychoice == "Y" or replaychoice == "y":
        rps_game()
    elif replaychoice == "N" or replaychoice == "n":
        exit()






#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
rps_game()
replay_rps()
