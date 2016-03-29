
#Stranded on an island is a program that will ask the user to make many choices, their choices will determine their survival on this uninhibited island.

a = raw_input("type your name here ")
print "Welcome to, Stranded on an Island"

print ("\n")

print "Hello " + str(a) + ", your ship have crashed and you have been stranded on island."

print ("\n")

print "Here you will have many choices to make, remember your survival depends on those choices."

print ("\n")

print "You see that both your knife and canteen have washed up onto shore with you, but you can only take one, which one do you pick?"

print ("\n")

choice_1 =raw_input("type your choice here ")

print("\n")

if choice_1 == "knife":
	print "great choice"
else: 
	print "sorry m8 you won't survive"
	exit()

print ("\n")

print "You hear a load roar close to you."
print "Do you go investigate the noise, or do you just stay?"

choice_2 = raw_input("stay, or go ")

if choice_2 == "stay":
	print "great choice"
else:
	print "You go over to investigate, you find out it's a large lion roaring, it attacks you and kills you." " You ded sorry m8"
	quit()

print("\n")

print "You start to feel hungry, you see some roots on the ground, do you eat it or not?"

choice_3 = raw_input("eat or not")






