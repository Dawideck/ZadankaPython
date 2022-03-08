#rekurencyjna silnia

n = int(input("podaj jaka silnie mam policzyc: "))


def rek_silnia(n):
	
	if n == 0:
		return 1
	else:
		return rek_silnia(n-1) * n



print(rek_silnia(n))
