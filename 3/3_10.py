import random
import math
import datetime


ptsInSquare = int(input("ile losujemy punktow?: "))
ptsInCircle = 0

now_time = datetime.datetime.now()

print(now_time)
print()

for i in range(ptsInSquare):
	x = random.uniform(-1.0, 1.0)
	#print(x)
	y = random.uniform(-1.0, 1.0)
	#print(y)
	if x*x + y*y <= 1:
		ptsInCircle += 1

r = ptsInCircle/ptsInSquare
pee = 4.0 * r

stop = datetime.datetime.now()

print("estymacja pi: ", +pee)
print("znane pi: ", +math.pi)
print()
roznica = math.pi - pee
print("roznica: ", roznica)
print()
print(stop)
print()
print("runtime: ", stop - now_time)
