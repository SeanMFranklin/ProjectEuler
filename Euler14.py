y = 0
l = 0
longest = 0
for i in range(1,1000000):
	x=i
	l=0
	while x != 1:
		if x%2 == 0:
			x/=2
		else:
			x= 3*x+1
		l+=1
	if l>longest:
		longest = l
		y = i
		print(str(y) + ": " + str(longest))
print(str(y) + ": " + str(longest))
