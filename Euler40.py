x = ''
for i in range(1000000):
	x+= str(i)

y = 1
for i in range(7):
	y*=int(x[10**i])
print(y)
