a = 1
def countup(a):
    if a >= 11:
        print "Blastoff!"
    else:
        print a 
        countup(a+1)

countup(a)
