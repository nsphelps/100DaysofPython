import random
import my_module

#Testing random number generator for integers
#random_int = random.randint(1, 10)
#print(random_int)

#Testing modules, not related to the rest of the file. 
#print(my_module.pi)

#Testing floats, always generates a number between 0 and 1. 
#random_float = random.random()
#print(random_float)

# Attempt at generating floating point numbers between 0 and 5
# This does work, but it may be worth looking at multiplying 
# the rand_flt by an integer which will also generate random
# floating point numbers.
#rand_int = random.randint(1, 5)
#rand_flt = random.random()
#rand_flt_point = rand_int + rand_flt
#print(rand_flt_point)

# This is a coin toss program for example
# toss = random.randint(0, 1)
#
# if (toss == 0):
#   print("Tails")
# else:
#   print("Heads")

# Practicing lists
# Create a list of states
#us_states = ["Colorado", "California", "Delaware", "Texas", "Georgia", "Alabama", "New York"]
# Generate a random number based on the number of states in the list minus 1 because we count starting at 0
#rand_num = random.randint(0, len(us_states)-1)
# Print the state that lives at the rand_num index
#print(us_states[rand_num])

# Practicing nested lists
#fruits=["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#dirty_dozen = [fruits, vegetables]

# Treasure Map Challenge
# The idea is to have three nested lists that form a sort of 'map'
# The user enters a postion (i.e. B3, C1, etc). From there, update
# the map with an 'X' in the user's input location. For example, 
# if the user enters 'B3' then we would update line3 at the [1] 
# index. 
#line1 = [" ", " ", " "]
#line2 = [" ", " ", " "]
#line3 = [" ", " ", " "]

#map = [line1, line2, line3]
#print("Hiding your treasure! X marks the spot.")
#position = input()
# Code below this point, don't change the code above
#row = int(position[1]) - 1
#col = position[0]

#if col == 'A':
#    col = 0
#elif col == 'B':
#    col = 1
#else:
#    col = 2

#map[row][col] = 'X'

# Code above this row, don't change code below
#print(f"{line1}\n{line2}\n{line3}")

# Above is my solution, below is the solution given in the class
# My solution did pass all of the programmed tests, however, it looks
# as though the 'desired' solution was more efficient. 
#letter = position[0].lower()
#abc = ['a', 'b', 'c']
#letter_index = abc.index(letter)
#number_index = int(position[1]) - 1
#map[number_index][letter_index] = "X"
#######################################################################