import math
high = 0
triangle = 1
k = 1
def numberofdivisors(x):
	global high
	z=[]
	y=0
	for i in range(1,int((x**.5+1))):
		if x%i==0:
			y+=2
			if x/i == i:
				y-=1
	if y>high:
		high = y
		print(str(high) +": " + str(x))
	return(y)

for i in range(15000):
	k+=1 
	triangle += k
	if numberofdivisors(triangle)>500:
		print(triangle)
		break
