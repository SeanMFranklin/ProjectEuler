x = []

for i in range(2,101):
	for j in range(2,101):
		x.append(i**j)


print(len(list(dict.fromkeys(x))))

