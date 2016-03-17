V1 = raw_input("type minimal number ")
V2 = raw_input("type maxium number ")

import random
def Target(V1,V2): 
	Target = (random.randint(int(V1),int(V2))) 
	return Target

print "I'm thinking of a number from " + int(V1) + " to " + int(V2)

print "What do you think that number is?"

user_guess = raw_input("type your guess ")

print "The target was " + str(Target(V1,V2))

print "Your guess was " + str(user_guess)


if user_guess > (Target(V1,V2)):
	result1 = int(user_guess) - (Target(V1,V2))
	print "That's over by " + str(result1)

else:
	 user_guess < (Target(V1,V2))
	result2 = (Target(V1,V2)) - int(user_guess)
	print "That's under by " + str(result2)

if user_guess == Target:
	print "Great guess, you are correct"
