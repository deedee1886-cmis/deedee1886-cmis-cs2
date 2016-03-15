V1 = raw_input("type minimal number ")
V2 = raw_input("type maxium number ")

import random
def target(V1,V2): 
	Target = (random.randint(int(V1),int(V2))) 
	return Target

print "I'm thinking of a number from " + V1 + " to " + V2

print "What do you think that number is?"

user_guess = raw_input("type your guess ")

print "The target was " + str(target(V1,V2))

print "Your guess was " + user_guess


if user_guess > target:
	result1 = user_guess - target
	print "That's over by" + result1

else:
	if user_guess < target:
		result2 = target - user_guess
	print "That's under by" + result2



