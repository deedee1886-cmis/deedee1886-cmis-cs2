import math
def add(a, b):
	return a + b
a1 = add(3, 4)
a2 = add(1, 2)
def sub(a, b):
	return a - b
b1 = sub(5, 3)
b2 = sub(1, 2)

def mul(a, b):
	return a * b
c1 = mul(4, 4)
c2 = mul(1, 2)
def div(a, b):
	return a / b
d1= div(2, 3)
d2 = div(1, 2)
def hours_from_seconds(a,b, c):
	return a/b/c
e1 = hours_from_seconds(86400,60,60)
e2 = hours_from_seconds(70000,60,60)
Areaofcircle=(5)
def volume_of_sphere(r):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2
g1 = 7
g2 = 14

def areaoftriangle (a,b,c):
	p = (a+b+c)/2
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

	Volumeofsphere=(5)
h1 = 20,40
h2 = 30,70

def averagevolume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2

averagevolume(5,10)

i1 = 20,40
i2 = 30,50

def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

areaoftriangle(1,2,2.5)

j1 = 2,2,2
j2 = 3,3,3

def right_align(a):
	return (a.rjust(80))
right_align("Hello")

k1 = right_align("cat")
k2 = right_align("lol")
def center(a):
	return (a.center(40))
center("Hello")

l1 = center("dog")
l2 = center("mouse")

def msgbox(a):
    return "+" + (len(a) + int(4)) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + int(4)) * "-" + "+"

o1 = msgbox("Hello")
o2 = msgbox("I eat cats!")


print msgbox(str(a1))
print msgbox(str(a2))
print msgbox(str(b1))
print msgbox(str(b2))
print msgbox(str(c1))
print msgbox(str(c2))
print msgbox(str(d1))
print msgbox(str(d2))
print msgbox(str(e1))
print msgbox(str(e2))
print msgbox(str(g1))
print msgbox(str(g2))
print msgbox(str(h1))
print msgbox(str(h2))
print msgbox(str(i1))
print msgbox(str(i1))
print msgbox(str(j1))
print msgbox(str(j2))
print msgbox(str(k1))
print msgbox(str(k2))
print msgbox(str(l1))
print msgbox(str(l2))

print o1
print o2 
