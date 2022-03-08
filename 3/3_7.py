#za pomoca for znajdz najwieksza i najmniejsza liczbe ze zbioru n wylosowanych liczb calkowitych 
#generowanych losow, w przedziale od 0 do 100, w przedziale <0;100> (n=5)
#oraz oblicz wartosc srednia ze wszystkich wylosowanych liczb

import random

liczba = []
n = int(input("podaj ilosc liczb: "))

max = 0
min = 0
sum = 0

i = 0
y = 0

for i in range(1, n):
	liczba.append(random.randint(0, 100))

min = liczba[0]
#print("i: ", +i)


print(liczba)
print()



for y in range(0, n-1):
	sum += liczba[y]

	if max < liczba[y]:
		max = liczba[y]
	if liczba[y] < min:
		min = liczba[y]
	print("min temp:", +min ,"max temp:", +max ,"y temp: ", +y)
	print("sumtemp:", +sum)
#print("y: ", +y)

print("min:", +min)
print("max:", +max)
print("sum:", +sum)
print("srednia:", sum/n)
