#suma zakresu z listy


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x = int(input("x: "))
y = int(input("y: "))

def sumacz_listowy(lista, x, y):
	
	if x > y:
		return 0
	else:
		return lista[x] + sumacz_listowy(lista, x+1, y)








print(sumacz_listowy(lista, x, y))
