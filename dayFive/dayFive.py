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

