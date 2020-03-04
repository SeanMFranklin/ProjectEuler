x=0
import math
for i in range(10000000):
	y = 0
	for j in str(i):
		y+=math.factorial(int(j))
	if i == y:
		x+=i
		print(i)
print(x)
