import numpy as np
print "This program will ask you for 5 integer or float value. It will calulate the average of all values from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."

first = raw_input("n0: ")
second = raw_input("n1: ")
third = raw_input("n2: ")
fourth = raw_input("n3: ")
fith = raw_input("n4: ")

if first >= 10:
	print "that number is out of range"

print np.mean(first, second, third, fourth, fith)
	
	







