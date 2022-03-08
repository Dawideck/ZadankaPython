a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = int(input("podaj c: "))

if a <= 0  or b <= 0 or c <= 0:
	print("nunu!!")

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
	print("To jest 3kat pitagorejski")
else:
	print("To nie jest 3kat pitagorejski")
