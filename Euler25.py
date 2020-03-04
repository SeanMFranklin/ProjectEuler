x = [1,1]
n=1
while len(str(x[n]))< 1000:
	n+=1
	x.append(x[n-1]+x[n-2])
print(x[0])
print(n)
print(len(x))

