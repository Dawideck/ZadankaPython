#sort list
import random

lista = []
k = int(input("podaj k:"))
#lista = [-460, 560, 325, 1, 3445, -999, 134, 37433, -134, -3498, 2]
for k in range(0, k, 1):
	lista[k] = random.randint(0, 100000)

def sortlista(lista):

	tempVar = 0
	listUnsorted = True


	for i in range(len(lista)-1, 0, -1):
		for j in range(i):

			if lista[j] > lista[j+1]:
				tempVar = lista[j]
				lista[j] = lista[j+1]
				lista[j+1] = tempVar
			print(lista)



	return lista








#sortlista(lista)
print(sortlista(lista))
