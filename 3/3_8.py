#for - wyswietlic tabliczke mnozenia 1 - 100

for wiersze in range(10):
	for kolumny in range(10):
		print((wiersze+1) * (kolumny+1), "\t" , end = "")
	print()
