#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)True 
#b)False
#c)If
#
#2) What does 'return' do?
#it returns a value, (display output)
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)If you don't indent when putting code into a variable, python will act like it's another set of code(not with the variable)
#b)
#Identation also makes your whole set of code more neat, and easier to read.
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 3
#problem1_b) square root of 3
#problem1_c) 0
#problem1_d) 5
#RIP brain
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) (1, 1.5)
#problem3_b) (1, 2)
#problem3_c) (1, 2)
#problem3_d) (1, 1)
#RIP
#problem4_a) (-2, -3, -4)
#problem4_b) (3, 2, 1)
#problem4_c) (0.5, 0.5, 0.5)
#problem4_d) 3
#lols can't do math

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

print "Type in 3 different numbers (decimals are OK!)"
A = raw_input("A ")
B = raw_input("B ")
C = raw_input("C ")

if A == B == C:
    print "you didn't follow directions"


else:
    foo = [A, B, C]
    print "The largest number was " + max(foo)

