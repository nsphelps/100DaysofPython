# For day four, we are asked to use what we have learned to create a rock, paper, scissors
# game that can be played against the computer. 
# Written By: Nick Phelps
# Date: May 21, 2024
#
# For this game, I decided to make use of the module I was practicing with earlier
# and create the ASCII art inside that module. This just help keep things cleaner IMHO. 
import random
import my_module

# Assign different ASCII art to choices
rock = my_module.rock
paper = my_module.paper
scissors = my_module.scissors

# Insert choices into a list
choice = [rock, paper, scissors]

print("Welcome to the Finger Dome! Prepare your rocks, papers, and scissors!")
print("Choose your weapon! (Type 0 for Rock, 1 for Paper, or 2 for Scissors)")

# Get user choice and convert to number, assign user_play to the choice index
# based on user input
user_num = int(input())
user_play = choice[user_num]
print(user_play)

# Generate a random integer, then set the computer choice index based on
# generated number
print("Your opponent chose:")
comp_num = random.randint(0, 2)
comp_play = choice[comp_num]
print(comp_play)

# Compare the user and computer plays to determine the winner
if user_num == comp_num:
    print("Disappointing...I wanted some sport, but its a draw.")
elif user_num == 0 and comp_num == 1:
    print("You lose!")
elif user_num == 0 and comp_num == 2:
    print("You win!")
elif user_num == 1 and comp_num == 0:
    print("You win!")
elif user_num == 1 and comp_num == 2:
    print("You lose!")
elif user_num == 2 and comp_num == 0:
    print("You lose!")
elif user_num == 2 and comp_num == 1:
    print("You win!")
else:
    print("Not a valid choice")