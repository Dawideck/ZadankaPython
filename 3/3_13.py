#l pierwsze 2-150 uzywajac all()
import math

pierwsze = []

for i in range(2, 1000001, 1):
	niedzielniki = []
	for j in range(2, int(math.sqrt(i))+1, 1):
		if i % j == 0:
			niedzielniki.append(False)
			break
		else:
			niedzielniki.append(True)

	if all(niedzielniki):
		pierwsze.append(i)



print(pierwsze)
