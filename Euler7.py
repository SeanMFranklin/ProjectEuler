x = [2,3]
i=0
while len(x)<10002:
	k = 0
	for j in range(2,int(i**(1/2)+1)):
		if i%j == 0:
			break
		elif j==int(i**(1/2)):
			x.append(i)
			print(len(x))
	i+=1

print(x[10000])
