#rekurencyjnie n liczb trojkatnych

n = int(input("podaj n>0: "))

def rek_trojkatne(n):
	if n <= 0:
		return 
	elif n == 1:
		print(f"{1} =")
		return 1
	else:
		print(f"{n} +")
		return rek_trojkatne(n-1) + n



print(rek_trojkatne(n))
