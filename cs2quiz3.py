#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that calls itself.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#A syntax error will pop up, since a recursive function needs a complete base case and recursive case in order to work properly.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#What you are going to put inside the base case, since the base case comes before the recursive case.
#
#
# 4) How do we put data into a function call?
#We first put data in a variable and put the variable in the function. EX- tester(data):
#
# 
# 5) How do we get data out of a function call?
#We call the function along with the variable. EX- tester(data)
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 12
#a2 = 12
#a3 = -1

#b1 = 9
#b2 = 0
#b3 = 0

#c1 = -5

#c2 = -7
#c3 = 34

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


import math

#base case
def adder(total):
	number = raw_input("type number ")
	if number == "":
		print "The sum is {}".format(total)
	else:
		total += float(number)
		adder(total)

#recursive case
def main():
	total = 0 

	adder(total)

	
main()


