sumofamicable = 0

def sumofdivisors(x):
	z=[]
	for i in range(1,int(x/2)+1):
		if x%i==0:
			z.append(i)
	return(sum(z))


for i in range(1,10000):
	if i == sumofdivisors(sumofdivisors(i)) and i != sumofdivisors(i):
		sumofamicable+=i
		print(str(i) + " : " + str(sumofdivisors(i)))

print(sumofamicable) 
