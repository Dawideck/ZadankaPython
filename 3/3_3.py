#while - suma parzysztych <1;100>

suma = 0
i = 1

while i <= 100:
	if i%2 == 0:
		suma = suma + i
	i += 1

print(suma)
