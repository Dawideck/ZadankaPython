#NWD reku

x = int(input("podaj x: "))
y = int(input("podaj y: "))


def NWD(x, y):
	if x%y == 0:
		return y
	else:
		r = x%y
		return NWD(y, r)


print(NWD(x, y))
