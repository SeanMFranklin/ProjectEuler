for i in range(500):
	for j in range(i):
		for k in range(j):
			if i + j + k == 1000 and k*k + j*j == i*i:
				print(i*j*k)
