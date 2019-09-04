# A python program to play Hand Cricket game with computer.

# Importing the random module.
import random

# The Toss
the_toss = True
# A while loop to check a valid toss happens.
while the_toss:
    player_call = input("Heads or Tails : \n").lower()
    toss=['heads','tails']
    coin = random.choice(toss)
    batting = ""
    # Checking if the user input is valid.
    if player_call == "heads" or player_call == "tails":
        # Checking if the user won the toss.
        if player_call.lower() == coin.lower():
            choose = input("Toss Won, Choose to bat or bowl : ").lower()
            if choose == "bat":
                batting = 'Player'
                the_toss = False
            else:
                computer_decision = "bat"
                batting = 'Computer'
                the_toss = False
        else:
            print("Toss lost, Computer chooses to : ")
            decision=["bat",'bowl']
            computer_decision = random.choice(decision)
            print(computer_decision)
            if computer_decision == "bat":
                batting = 'Computer'
                the_toss = False
            else:
                batting = 'Player'
                the_toss = False
    else:
        print("\nEnter a valid call")

# Validating basic variables for future loop use.
innings = 1
computer_score=0
player_score=0

# Function to check who won the game.
def check(score_1,score_2):
    if score_1 > score_2:
        print("Player is the winner!")
    elif score_2 > score_1:
        print("Computer is the winner!")
    elif score_1 == score_2:
        print("Match Draw!")

# The main place where the game happens.
# A while loop to check that only 2 innings are being played.
while(innings<3 and innings>0):
    # A while loop for when the computer is batting.
    while batting == "Computer" and innings < 3:
        player_ball = int(input("Bowl your ball : "))
        # A if condition so that no illegal balls are being bowled.
        if player_ball in range(1,7):
            computer_run = random.randint(1, 6)
            print("Computer run : {}".format(computer_run))
            if computer_run == player_ball:
                print("\nComputer Out!\nComputer score : {}".format(computer_score))
                if innings == 2:
                    check(player_score,computer_score)
                elif innings == 1:
                    player_target = computer_score +1
                    print("The Target for you is {}\n".format(player_target))
                innings += 1
                batting = "Player"
            else:
                computer_score += computer_run
                # An if condition for checking if the computer has reached the target in the 2nd innings.
                if innings == 2 and computer_score > player_score:
                    check(player_score, computer_score)
                    innings += 1
        else:
            print("Enter a valid ball in range (1-6) ")

    # A while loop for when the player is batting.
    while batting == "Player" and innings <3:
        player_run = int(input("Bat : "))
        # An if condition to keep in check that the player doesn't cheat.
        if player_run in range(1,7):
            computer_ball = random.randint(1,6)
            print("Computer ball : {}".format(computer_ball))
            if player_run == computer_ball:
                print("\nPlayer Out!\nPlayer score : {}".format(player_score))
                if innings == 2:
                    check(player_score,computer_score)
                elif innings == 1:
                    computer_target = player_score + 1
                    print("The target for Computer is {}\n".format(computer_target))
                innings +=1
                batting = "Computer"
            else:
                player_score += player_run
                # An if condition to check if the player has reached the target set by the computer.
                if innings == 2 and computer_score < player_score:
                    check(player_score, computer_score)
                    innings += 1
        else:
            print("Play the ball in range(1-6)")


