x=[]
x.append(1)
x.append(1)
n = 1
ans = 0
while x[n] <4000000:
	print(x[n])
	if x[n]%2 == 0:
		ans += x[n]
	n += 1
	x.append(x[n-1]+ x[n-2])
print(ans)
	
