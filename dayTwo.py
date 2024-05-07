# Day Two: Today was all about learning different data types, mathematics, and f-Strings
# Written By: Nick Phelps
# Date: April 23, 2024

# In today's project, we are creating a basic tip calculator. The idea is to input the total of a bill,
# the tip percentage that you want to leave, and the number of people who will be splitting the bill.
# Then, some calculations are done and the total per person should be output to the user.

# Print greeting to the user
print("Welcome to the tip calculator!")

# Prompt the user for the total cost of the bill
# Keep in mind that purchases are rarely even dollar amounts and that there is usually some value to the 2nd decimal
# place which means that we should use a floating point value for this variable
bill = float(input("What is the total cost of the bill? $"))

# Prompt the user for the tip amount
# Additional computation is done to convert the integer input into a percentage that will be added to
# the total cost of the bill.
tip = int(input("How much would you like to tip? 10, 12, 15, or 20? "))
tip = (tip / 100) + 1

# Prompt the user to input the number of people who will be splitting the bill
split = int(input("How many people will split the bill? "))

# Calculate the per-person total by multiplying the bill by the tip and dividing by the split.
per_person_total = (bill * tip) / split

# Then format the per-person total to two decimal places
amt_per_person = "{:.2f}".format(per_person_total)

# Print the per-person total to the user
print(f"Each person should pay: ${amt_per_person}")
