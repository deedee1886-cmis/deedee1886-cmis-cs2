print "Type in 3 different numbers (decimals are OK!)"
A = raw_input("A ")
B = raw_input("B ")
C = raw_input("C ")

if A == B == C:
    print "you didn't follow directions"


else:
    foo = [A, B, C]
    print "The largest number was " + max(foo)




