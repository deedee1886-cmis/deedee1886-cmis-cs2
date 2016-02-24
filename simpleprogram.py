def info():
	a = raw_input("type your height here: ")
	return a
def height_in_inches():
	height_in_inches = float(info()) * 0.39370
	return height_in_inches
	

def your_height_vs_average_height():
	your_height_vs_average_height = float(height_in_inches()) - 69
	return your_height_vs_average_height

print "you are " + str(height_in_inches()) + " inches tall " + str(your_height_vs_average_height()) + " is your height compared to the average height (69 inches)" 
#if the number returned is positive, that means you are that much taller than the average height, if the number returned is negative, then that means you are that much shorter than average height


