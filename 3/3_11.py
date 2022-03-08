#1000 - 9999 wyszukaj liczby spelniajace ciekawa zaleznosc 1233 = 12^2 + 33^2

def main():

	lista = []

	for i in range(1000, 10000, 1):

		n=str(i)
		digits=[int(x) for x in str(n)]

		a=n[0]+n[1]
		a=int(a)
	
		b=n[2]+n[3]
		b=int(b)
		akw = a*a
		bkw = b*b
		n=int(n)

		if akw+bkw == n:
			print("ok")
			lista.append(n)
		else:
			print("nieok")
			print(f"akw: {akw} bkw: {bkw}")
		print(f"a:  {a}, b:  {b}, n:  {n}")

	print(lista)

main()

