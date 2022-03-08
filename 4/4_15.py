#lambda x^2 = 1, co 0.5


fun = lambda x: x*x+1


krok = 0.5
x = 0

while x <= 5:
	wynik = fun(x)
	print(wynik)
	x = x + krok



