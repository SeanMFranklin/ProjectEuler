x = 0
k=0
l=0
i=1
dim = 1001
while i < (dim**2+1):
	x+=i
	if (l)%4==0:
		k+=2
	print(i)
	l+=1
	i+=k
print(x)
