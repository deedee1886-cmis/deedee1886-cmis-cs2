import math
def add(a, b):
	return a + b
add(3, 4)

def sub(a, b):
	return a - b
sub(5, 3)

def mul(a, b):
	return a * b
mul(4, 4)

def div(a, b):
	return a / b
div(2, 3)

def hours_from_seconds(a,b, c):
	return a/b/c
hours_from_seconds(86400,60,60)

Areaofcircle=(5)
def volume_of_sphere(r):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2


def areaoftriangle (a,b,c):
	p = (a+b+c)/2
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

	Volumeofsphere=(5)

def averagevolume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2

averagevolume(5,10)

def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

areaoftriangle(1,2,2.5)

def right_align(a):
	return (a.rjust(80))
right_align("Hello")

def center(a):
	return (a.center(40))
center("Hello")

def msgbox(a):
    return "+" + (len(a) + int(4)) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + int(4)) * "-" + "+"

msgbox("Hello")
msgbox("I eat cats!")


