from math import factorial

def nCr(n,r):
	return(factorial(n)/(factorial(r)*factorial(n-r)))

count = 0
for i in range(1,101):
	for j in range (1,i):
		if nCr(i,j) > 1000000:
			count += 1

print(count)
