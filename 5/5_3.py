#obiektowo tablica 10x10, na przekatnej liczby <0;9>, reszta 0. oblicza sume na przekatnej

import random


class Tablica:

	def __init__ (self):

		print("Obiekt stworzony. Zaraz wypisze tablice.")



	def fill (self, dim, tablica):

		suma = 0

		for i in range(dim):
			for j in range(dim):
				if i == j:
					liczba = random.randint(0,9)
					tablica[i][j] = liczba
					suma += liczba
				else:
					tablica[i][j] = 0

		print(suma)

		for i in range(dim):
			for j in range(dim):
				print(tablica[i][j], " ", end="")
			print()







dim = int(input("Podaj rozmiar tablicy: "))
tablica = [[0 for i in range(dim)] for j in range(dim)]
#print(tablica)


t = Tablica()
t.fill(dim, tablica)



