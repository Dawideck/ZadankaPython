#1000 - 9999 wyszukaj liczby spelniajace ciekawa zaleznosc 1233 = 12^2 + 33^2

def main():

	j=0
	lista = []

	for i in range(100000, 1000000, 1):

		n=str(i)
		digits=[int(x) for x in str(n)]

		a=n[0]+n[1]+n[2]
		a=int(a)
	
		b=n[3]+n[4]+n[5]
		b=int(b)
		akw = a*a
		bkw = b*b
		n=int(n)

		if akw+bkw == n:
			#print("ok")
			lista.append(n)
			j += 1
		#else:
			#print("nieok")
			#print(f"akw: {akw} bkw: {bkw}")
		#print(f"a:  {a}, b:  {b}, n:  {n}")

	print(lista)

main()

