import math
import random
#Stranded on an island is a program that will ask the user to make many choices, their choices will determine their survival on this uninhibited island.

a = raw_input("type your name here :")
print "Welcome to, Stranded on an Island"

print ("\n")

print "Hello " + str(a) + ", your ship have crashed and you have been stranded on island."

print ("\n")

print "Here you will have many choices to make, remember your survival depends on those choices."

print ("\n")

print "You see that both your knife and canteen have washed up onto shore with you, but you can only take one, which one do you pick?"

print ("\n")

choice_1 =raw_input("type your choice here :")

print("\n")

if choice_1 == "knife":
	print "great choice"
else: 
	print "sorry m8 you won't survive"
	exit()

print ("\n")

print "You hear a load roar close to you."

print "Do you go investigate the noise, or do you just stay?"

print("\n")

choice_2 = raw_input("stay, or go :")

if choice_2 == "stay":
	print "great choice"
else:
	print "You go over to investigate, you find out it's a large lion roaring, it attacks you and kills you." " You ded sorry m8"
	quit()

print("\n")

print "You start to feel hungry, you see some roots on the ground, do you eat it or not?"

print("\n")

choice_3 = raw_input("eat or not :")

if choice_3 == "eat":
	print "good choice, you grab some roots, and eat them, this gives you a slight energy boost."

else:
	print "You don't eat the roots, you then die of hunger"
	quit()


print("\n")

print "After eating the roots, you see a crazy man screaming, jarate in the left hand, and a spear in the other"

print "Do you go and talk to the crazy man or do you run away?"

print("\n")

choice_4 = raw_input("talk or run :")

print("\n")

if choice_4 == "talk":
	print "You go towards the man and try to communicate with him, he sees you as a friend in need, so he proceeds throws his jarate at you. The jarate breaks instantly upon inmpact, the substances, cover your body, giving you super powers."

else: 
	print "You get scared of the crazy man, and you attempt to run away, he throws his spear at you, the spear penetrates you through the back, killing you instantly."
	quit()

print("\n")

print "You see a navy ship approching you, there are many soldiers on board."

print "Do you wave your hands at the ship, or do you enbrace the jarate, and harness the power of the jarate god?"

print("\n")

choice_5 = raw_input("wave or embrace :")

print("\n")

if choice_5 == "wave":
	print "You wave your hands at the ship, the soldiers aboard see you and they start to send men down to the soil. The men approach you, a feeling of relief starts to form. However the men start shouting, one of the soldiers pulls out his taser, and shoots you right in the gut, the taser shot incapitates you, putting you on the sand. Two weeks later, you are watching the tv, in your cell, on the tv the headline read, world class drug dealer with alzheimers caught on a deserted island."
	quit()

else:
	print "You pray to the jarate god, and embrace your innner jarate form, this gives you even more power, you use your new found powers to take down the soldiers and their ship."

print "You manage to fend off the soldiers, you get to live another day, however the jarate god is mad at your actions. A few hours later, you notice the sea turning yellow, and you could also smell a nasty stench in the air, before you knew it, the newly colored sea, swallows you whole. You then get sent to the heavens, where you meet the jarate god."



print "In the heavens the jarate god invites you to play some games with him."

print("\n")

print "The jarate go has you roll a dice, if you roll a one you will continue playing his games, if you roll a two, then he will banish you from his kingdom."

print("\n")


x = number = random.randint(1, 2)

print x

if x == 1:
	print "You have rolled and one, and the jarate god is pleased."

elif x == 2:
	print "You have rolled a two, and the jarate god is mad at you, he proceeds to banish you from the heavens."
	quit()

print("\n")

print "Since you have survived this long, the jarate god gives you 100 dollars."

print("\n")

subtraction == 100 - 3.5 

print("\n")

print "A tax collector comes over and asks you for a payment of 3.5 dollars, do you give him the money or do you attempt to run away from him."

choice_6 = raw_input("run or give")

if choice_6 == "run":
	print "As you run away from the tax collector, you run into a big man, he gets mad at you, and beats you up."

else:
	print subtraction



