a = 100
def countdown(a):
	if a < 0:
		print "BlastOff!"
	else:
		print a
		countdown(a-1)
