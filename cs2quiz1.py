#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#That symbol is called a assignment operator, it creates new variables, and gives the variables values. 
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a named set of code that peforms a computation.
#
#
#3 1pt) What does the keyword "return" do?
#The keyword return, calls the function, after being called the function takes an argument and returns a result. This result is called a return value.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1:int = 2   3
#	2:str = "hello"   "testing"
#	3:float = 2.346   3.14
#	4:bool = True   False
#	5:tupple = ("My name is DeeDee", "I am", 14, "years old") ("I like dogs", "I have" 3 "dogs")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function definiton is just defining the fucntion, while a function call is the calling the actual function with numbers or strings.
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input
#	2:process
#	3:output
#
#Part 2: Programming (25 points)
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

def circle_diameter(area):
    return math.sqrt(((area) / math.pi)) + math.sqrt(((area) / math.pi))

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


