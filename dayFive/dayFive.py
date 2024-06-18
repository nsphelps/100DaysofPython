# Day five is primarily about loops, specifically the FOR loop.
# Here is an example of a for loop that iterates over a list 
# and prints out each item in the list

#fruits = ["apple", "bannana", "cherry"]
#for fruit in fruits:
#    print(fruit)  # Pay attention to the indentation inside the loop
#    print(fruit + " pie")  # this is a simple way to concatenate new data to a variable inside a loop


# Interactive challenge 1: Average Height
# Input a Python list of student heights
#student_heights = input().split()
#for n in range(0, len(student_heights)):
#    student_heights[n] = int(student_heights[n])
# Don't change the code above ^^
#sum_height = 0  # Initialize a local variable to store the sum of all the list values
#avg_height = 0  # Initialize a local variable that will store the average height

#for i in student_heights:   # For loop that iterates over the length of the list and adds the values to the local variable
#    sum_height += i

#avg_height = sum_height / len(student_heights)

# Generate the output in the following statements
#print("total height = " + str(sum_height))
#print("number of students = " + str(len(student_heights)))
#print("average height = " + str(round(avg_height)))
# I need to be better about using f strings
#print(f"average height = {avg_height}")
################################################################################################################################
# Interactive challenge 2: High Score
# Write a program that calculatees the highest score from a List of scores.
# e.g. student_score = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min funtions. The output
# words must match the example. i.e
# The highest score in the class is: x

# Input a list of student scores
#student_scores = input().split()
#for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
# Write your code below this line ############
#high_score = 0  # Initialize some local variables to hold the scores
#temp_score = 0

#for i in student_scores:   # For loop that iterates over each of the list indicies
#    temp_score = i         # Store the current index as the temp_score
#    if temp_score > high_score:   # Compare the temp_score with the current high_score
#        high_score = temp_score   # If temp_score is greater, it becomes the new high_score
# Above is my code which did pass, however, there was a more efficient way of writing it that I want to put below
#for score in student_scores:
#    if score > high_score:
#        high_score = score
# ^^ This eliminates both the need for a second local variable and setting the temp_score value

#print(f"The highest score in the class is: {high_score}")

# For loops with the range() function
#for number in range(1, 11, 3):  # range() does not include the final digit from 1-10 (i.e 1,2,..9)
#    print(number)
#total = 0
#for number in range(1, 101):
#    total += number
#print(total)
#######################################################################################################################################
# Interactive challenge 3: Adding Even Numbers
# Write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and 
# the last one is 100: i.e 2+4+6_8_10...+98+100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of
# the calculation. Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

#target = int(input()) # Enter a number between 0 and 1000
### Dont change the code above ###
#total = 0
#target += 1
#for i in range(0, target, 2):
#    total += i

#print(total)
#########################################################################################################################################
# Interactive challenge 4: Fizzbuzz
# Write a program that automatically prints the solution to the FizzBuzz game. These are the rules of FizzBuzz game:
#   - Print each number from 1 to 100 in turn and include the number 100
#   - When the number is divisible by 3 then instead of printing the number it should print "Fizz"
#   - When the number is divisible by 5 then instead of printing the number it should print "Buzz"
#   - And if the number is divisible by both 3 and 5 then it should print "FizzBuss"

#target = 100

#for i in range(1, target + 1):
#    if ((i % 3 == 0) and (i % 5 == 0)):
#        print('FizzBuzz')
#    elif (i % 3 == 0):
#        print('Fizz')
#    elif (i % 5 == 0):
#        print('Buzz')
#    else:
#        print(i)

#########################################################################################################################################

# Final Project for Day 5
#
# The PyPassword Generator will have a few different prompts for the user to enter the length of the desired password, the number of 
# special characters and how many numbers they would like. 
import random

# First, I set up a few lists that have different letters, numbers, and special characters
#letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#characters = ['!', '@', '#', '$', '%', '^', '&', '?', '<', '>']

# Initialize a password list and string
#userPass = []  # Used to hold the randomly generated characters
#password = ""  # The userPass list will be used to randomly generate the password string

# Prompt user for desired password length, number of special characters and number of integers
#desired_len = int(input("How many characters would you like your password to be?\n"))
#num_char = int(input ("How many special characters would you like in your password?(i.e @, #, etc)\n"))
#num_int = int(input ("How many numbers would you like in your password?\n"))

# Iterate over the desired password length
#for i in range(1, desired_len + 1):
    # Randomly select which list to pull from as long as there are more special characters or numbers to generate
#    while (num_char != 0) or (num_int != 0):
#        rand_entry = random.randint(1, 3)  # Generate a random number between 1-3
        
        # If 1, generate a random special character and add it to the userPass list
#        if rand_entry == 1:
#            if (num_char != 0):
#                rand_char = random.choice(characters)
#                userPass.append(rand_char)
#                num_char -= 1
        # If 2, generate a random number and add it to the userPass list
#        elif rand_entry == 2:
#            if (num_int != 0):
#                rand_int = random.choice(numbers)
#                userPass.append(rand_int)
#                num_int -= 1
        # Otherwise, generate a random letter and add it to the userPass list
#        else:
            # Flip a coin to determine if the letter should be upper or lower-case
#            flip_coin = random.randint(1, 10)
            # Between 1-5, lower-case
#            if flip_coin in range(1, 5):
#                rand_letter = random.choice(letters)
#                rand_lower = rand_letter.lower()
#                userPass.append(rand_lower)
            #Otherwise, upper-case
#            else:
#                rand_letter = random.choice(letters)
#                userPass.append(rand_letter)

# Continue appending random letters if / when the number of desired special characters / numbers is fulfilled
#while len(userPass) != desired_len:
#    flip_coin = random.randint(1, 10)
#    if flip_coin in range(1, 5):
#        rand_letter = random.choice(letters)
#        rand_letter = rand_letter.lower()
#        userPass.append(rand_letter)
#    else:
#        rand_letter = random.choice(letters)
#        userPass.append(rand_letter)

# Used for testing, prints the userPass list
#print(userPass)

# Construct a random password based on the userPass list
#for i in range(1, len(userPass) + 1):
#    rand_char = random.choice(userPass) # Chose a random character inside the userPass list
#    password += rand_char               # Add the random character to the password string
#    userPass.remove(rand_char)          # Remove the previous random character from the userPass list options

# Print the generated password to the user
#print("Your PyPassword is: " + password)

# Some key notes learned, use the random.choice funtion to select a random entry in a list
# For example, random.choice(letters) could be used instead of having the 'x = random.randint(1, 10)...'
# Basically, this ^^ just cleans up the code and makes it more efficient. 
# Another lesson, I over complicate a lot of things...