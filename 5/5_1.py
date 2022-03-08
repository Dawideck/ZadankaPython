#obiektowo obliczanie pola prostokata, metody czytaj, przetworz, wyswietl


class Prostokat:

	def __init__(self):
		
		self.a = 0
		self.b = 0
		self.pole = 0

	def __del__(self):
		
		print("deleted")


	def czytaj_dane(self):

		self.a = float(input("Podaj bok a prostokata: "))
		self.b = float(input("Podaj bok b prostokata: "))


	def przetworz_dane(self):

		self.pole = self.a * self.b


	def wyswietl_dane(self):

		print(f"Pole prostokata {self.a}x{self.b} ,to: {self.pole}")



prstkt = Prostokat()
prstkt.czytaj_dane()
prstkt.przetworz_dane()
prstkt.wyswietl_dane()

del prstkt
