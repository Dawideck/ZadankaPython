import math

a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))

if a == 0 and b != 0:
	print(f"to jest funkcja liniowa z miejscem zerowym: {(-c/b):.2f}")
elif a == 0 and b == 0:
	print(f"to jest funkcja stala: {c:.2f}")
else:
	delta = (b*b)-(4*a*c)
	print(delta)
	if delta < 0:
		print("delta<0 brak miejsc zerowych")
	elif delta == 0:
		print(f"jedno miejsce zerowe: {-b/(2*a):.2f}")
	else:
		print(f"miejsca zerowe, to x1 = {(-b - math.sqrt(delta)) / 2*a:.2f} oraz x2 = {(-b + math.sqrt(delta)) / 2*a:.2f}")
