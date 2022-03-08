#suma do n + - 


n = int(input("podaj n: "))



def suma(n):
	
	sum = 1

	for i in range(2, n + 1):

		if i % 2 == 0:
			sum = sum + i
			#print(sum)
		else:
			sum = sum - i
			#print(sum)

	return sum






print(suma(n))

