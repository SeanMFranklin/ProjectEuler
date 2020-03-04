x = 600851475143
big = 1
for i in range(100):
	if x % (i+1) == 0:
		x/= (i+1)
	for j in range(20):
		if x % (j+1) == 0:
			x/= (j+1)
for i in range(100000):
	if x % (i+1) == 0:
		big = (i+1)
		x/= (i+1)
print(big)
