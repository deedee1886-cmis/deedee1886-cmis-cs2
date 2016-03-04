#-9.5 --> 30.5/40
#Part 1: Terminology (15 points) -3.5 --> 11.5/15
#1 1pt) What is the symbol "=" used for?
#That symbol is called a assignment operator, it creates new variables, and gives the variables values. 
#1pt
#
#2 3pts) Write a technical definition for 'function'
#A function is a named set of code that peforms a computation.
#3pt
#
#3 1pt) What does the keyword "return" do?
#The keyword return, calls the function, after being called the function takes an argument and returns a result. This result is called a return value.
# 1pt
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1:int = 2   3
#	2:str = "hello"   "testing"
#	3:float = 2.346   3.14
#	4:bool = True   False
#	5:tupple = ("My name is DeeDee", "I am", 14, "years old") ("I like dogs", "I have" 3 "dogs")
#5pt
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function definiton is just defining the fucntion, while a function call is the calling the actual function with numbers or strings.
#0pt (reused "define" and "call" didn't really explain)
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input
#	2:process
#	3:output
#1.5pt (didn't explain what happens)
#
#Part 2: Programming (25 points) - 6 --> 19/25
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
#input
import math

C1 = raw_input("Area of C1: ")
C2 = raw_input("Area of C2: ")
C3 = raw_input("Area of C3: ")

#1 pt for header line
#3 pt for correct formula
#1 pt for return value
#1 pt for parameter name
#1 pt for function name
def circle_diameter(area):
    return math.sqrt(((area) / math.pi)) + math.sqrt(((area) / math.pi))

#NO OUTPUT FUNCTION
#-1pt for header line
#1pt for parameter names
#1pt for return value
#1pt for correct output format
#-3pt for correct use of format function

#NO MAIN FUNCTION
#-1pt header line
#1pt getting input
#1pt converting input
#-1pt for calling output function
#2pt for correct diameter formula
#1pt for variable names

#-1pt for calling main

print ""
#processing
CD1 = math.sqrt(((float(C1)) / math.pi)) + math.sqrt(((float(C1)) / math.pi))
CD2 = math.sqrt(((float(C2)) / math.pi)) + math.sqrt(((float(C2)) / math.pi))
CD3 = math.sqrt(((float(C3)) / math.pi)) + math.sqrt(((float(C3)) / math.pi))

Total = float(CD1) + float(CD2) + float(CD3)
#output
print "Circle  Diameter"
print "c1      " + str(CD1)
print "c2      " + str(CD2)
print "c3      " + str(CD3)
print "Totals  " + str(Total)

#1pt explanatory comments
#1pt code format
