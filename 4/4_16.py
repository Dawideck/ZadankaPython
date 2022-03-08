#iteracyjnie znalezc trojkaty pitagorejskie do N

lista = []

N = int(input("podaj N: "))



def znajdz_trojki(N):
	for i in range(1, N):
		for k in range(1,N):
			for l in range(1, N):
				if i*i + k*k == l*l:
					print(i, k, l)
					print('-' * 10)
	return lista






znajdz_trojki(N)
