# The objective of this project is to complete https://reeborg.ca/ maze challenge
# This project randomly generates reeborgs location as well as the direction they
# are facing and asks us to help him find the end. To do this, we are asked to 
# follow the right wall until to find the end. If there is no wall on the right,
# turn right and move forward, continue moving forward so long as the wall is on
# the right and the path forward is clear. If there is a wall on the right and
# the path forward is blocked, turn left as a last resort. Below is the code that
# I wrote that was able to solve the maze.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()