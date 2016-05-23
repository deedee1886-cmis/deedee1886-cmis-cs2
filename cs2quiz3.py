#Section 1: Terminology
# 1) What is a recursive function?
#A recursive function is a function that calls itself.
#correct
#
# 2) What happens if there is no base case defined in a recursive function?
#A syntax error will pop up, since a recursive function needs a complete base case and recursive case in order to work properly.
#correct
#
# 3) What is the first thing to consider when designing a recursive function?
#What you are going to put inside the base case, since the base case comes before the recursive case.
#correct
#
# 4) How do we put data into a function call?
#We first put data in a variable and put the variable in the function. EX- tester(data):
#correct
# 
# 5) How do we get data out of a function call?
#We call the function along with the variable. EX- tester(data)
#correct
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 12 #incorrect
#a2 = 12 #incorrect
#a3 = -1 #correct

#b1 = 9 #incorrect	
#b2 = 0 #incorrect
#b3 = 0 #incorrect

#c1 = -5 #incorrect
#c2 = -7 #incorrect
#c3 = 34 #incorrect

#d1 = 6 #correct
#d2 = 8 #correct
#d3 = 4 #correct

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


import math

#base case 2/2
def adder(total):
	number = raw_input("type number ")
	if number == "":
		print "The sum is {}".format(total) #it returns the sum +1
	else:
		total += float(number)               #it does not filter even numbers 0/2
		adder(total)			     #the function does increments properly 1/1

#recursive case 2/2				     #did not use return 0/1
def main():
	total = 0 				     #main function is defined and is also called 1/1

	adder(total)

	
main()


