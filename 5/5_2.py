#3mian kwadratowy obiektowo

import math


class Trojmian:

	def __init__ (self):

		self.a = 0
		self.b = 0
		self.c = 0
		self.x0 = None
		self.x1 = None
		self.x2 = None


	def czytaj_i_przetworz(self):

		while True:
			self.a = float(input("Podaj a: "))
			if self.a == 0:
				print("ej, to bedzie liniowka!")
			else:
				break

		self.b = float(input("Podaj b: "))
		self.c = float(input("Podaj c: "))

		self.delta = (self.b * self.b) - (4 * self.a * self.c)
		print(self.delta)

		if self.delta < 0:
			print("Brak miejsc zerowych")
		elif self.delta == 0:
			self.x0 = -self.b/2 * self.a
			print(f"Jedno miejsce zerowe x0={self.x0:.2f}")
		elif self.delta > 0:
			self.x1 = (-self.b -math.sqrt(self.delta))/(2 * self.a)
			self.x2 = (-self.b +math.sqrt(self.delta))/(2 * self.a)
			print(f"2 miejsca zerowe: x1={self.x1:.2f} i x2={self.x2:.2f}")




kwadratowa = Trojmian()
kwadratowa.czytaj_i_przetworz()
