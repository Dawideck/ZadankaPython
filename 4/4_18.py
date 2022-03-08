#1+3+5+7+(2*n-1)


n = int(input("podaj n: "))

def sumka_nparz(n):
	
	s = 0

	for i in range(1, n+1):

		if i % 2 != 0:
			s = s + 2 * i - 1


	return s


print(sumka_nparz(n))
