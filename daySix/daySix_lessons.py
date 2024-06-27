# Today's lesson is all about code blocks, functions, and while loops

# Some important about functions docs: docs.python.org/3/library/functions.html

# To make your own functions, first you start with a key word 'def'
# Everything that comes after the colon and is indented is part of the function
def my_funct():
    print("Hello")
    print("Goodbye")

# In order to run the function, we need to call it
# This will call the function and print the two strings
my_funct()

# Basic function structure
#    def my_function():   # Define the function 
#        Do something
#        Then do something else
#        Finally do this
# Then you need to call the function
#    my_function()

# This link can be used to help understand functions and practice writing your own
# to solve simple challenges:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Indentions are important for code blocks. They are used for everything from loops, to if-else statements, to functions. 
# Think of it like a file tree, each file is held within a folder. If it is in the folder it is indented. 
# There are two ways to create indentation, spaces and tabs. There is some debate about which is better, however,
# once it is compiled it doesn't really matter. (Spaces are better)

# Moving on to while loops
# The basic idea is that the loop will continue so long as some condition is true
# In comparison to the For loop, which uses for something in something (list, range, etc), do some thing
# a While loop has something like while some_num > 5: (indent) do something, then some_num -= 1
# This is a more accurate representation of the While loop structure
# num = 5
# while num > 0:
#    print("Hello there")
#    num -= 1
# This keeps the loop printing "Hello there" until num = 0 because 0=0 is not 0>0 so the loop would be false and break
# Be watchful for infinite loops, this means your while loop condition is never met and continues forever

# From the reeborg.org Hurdle3 challenge3
# This challenge asks us to move the robot, in the most efficient way,
# to the goal when we don't know where walls are / where the goal is. 
#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()

#def jump():
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()

#while not at_goal():
#    if wall_in_front():
#        jump()
#    else:
#        move()

# From the reeborg.org Hurdle4 challenge:
# This is similar to the third except that the hurdles have variable heights
# I had to modify the jump() function a bit with some extra while loops
#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
    
#def jump():
#    turn_left()
#    while wall_on_right():
#        move()
#    turn_right()
#    move()
#    turn_right()
#    while not wall_in_front():
#        move()
#    turn_left()

#while at_goal() != True:
#    if wall_in_front():
#        jump()
#    else:
#        move()