def digitsum(x):
	y = 0
	for i in str(x):
		y+=int(i)
	return y

max = 0

for i in range(100):
	for j in range(100):
		if digitsum(i**j) >max:
			max = digitsum(i**j)

print(max)
