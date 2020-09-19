def main():
	a = int(input("Enter a number here: "))
	b = int(input("Enter another number here: "))

	sums = addTwo(a,b)
	minus = subTwo(a,b)
	muls = mulTwo(a,b)
	divs = divTwo(a,b)
	print("sum: {}, subs: {}, multi: {}, division: {}".format(sums,minus,muls,divs))

def addTwo(x,y):
	sums = x + y
	return sums

def subTwo(x,y):
	subs = x - y
	return subs

def mulTwo(x,y):
	muls = x * y
	return muls

def divTwo(x,y):
	divs = x/y
	return divs


