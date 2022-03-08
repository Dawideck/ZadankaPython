#for - print caly alfabet uppercase w przod i tyl
import string

alfabet =string.ascii_uppercase
rev_alfabet = string.ascii_uppercase
"""alfabet = list(map(chr, range(97,123)))
alfabet.upper()
print(alfabet)
"""
#print(alfabet)

for i in range(26):
	print(alfabet[i], end=" ")

for j in range(25, -1, -1):
	print(alfabet[j], end=" ")
