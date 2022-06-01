#Rock Paper Scissor game. 

#Add random to generate the random choice for the computer player. 

import random

exit = False
user_points = 0
computer_points = 0

#Make a while loop and making the user select an option or quit. The computer input will use the random module to choose an option.

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors. Type exit to leave the game: ")
    computer_input = random.choice(options)

#if the users enters exit, the loop will break and show you the final score between the player and computer

    if user_input == "exit": 
        print("Game Ended")
        print("You won a total score of "+ str(user_points) +"and the computer's total score is "+ str(computer_points))
        exit = True

#If/Else/Elif statements for user input of rock

    if user_input == "rock":
        if computer_input == "rock": 
            print("Your selection is rock")
            print("The CPU input is rock")
            print("It's a tie!")
        elif computer_input == "paper":
            print("Your selection is rock")
            print("The CPU input is rock")
            print("You lose this round, CPU wins!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your selection is scissors")
            print("The CPU input is rock")
            print("You win!")
            user_points += 1

#If/Else/Elif statements for user input of paper

    elif user_input == "paper": 
        if computer_input == "rock": 
            print("Your selection is paper")
            print("The CPU input is rock")
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your selection is paper")
            print("The CPU input is paper")
            print("It's a tie!")
        elif computer_input == "scissors":
            print("Your selection is paper")
            print("The CPU input is scissors")
            print("You lose this round, CPU wins!")
            computer_points += 1

#If/Else/Elif statements for user input of scissors

    elif user_input == "scissors":
        if computer_input == "rock": 
            print("Your selection is scissors")
            print("The CPU input is rock")
            print("You lose this round, CPU wins!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your selection is scissors")
            print("The CPU input is paper")
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("Your selection is scissors")
            print("The CPU input is paper")
            print("It's a tie!")

#elif statement for invalid entries from the user

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors": 
        print("Invalid entry, please try again")