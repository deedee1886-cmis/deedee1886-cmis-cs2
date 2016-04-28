import math

def adder(total):
	number = raw_input("type number ")
	if number == "":
		print "the sum is {}" .format (number)
	else:
		total += float(number)
		adder(total)

def main():
	total = 0 

	adder(total)

	
main()






