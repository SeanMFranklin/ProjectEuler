

def primecheck(x):
	for i in range(2,int(x**.5)+1):
		if x%i == 0:
			return False
	return True
	
def circular(x):
	x = str(x)
	for i in range(len(x)):
		if not primecheck(int(x)):
			return False
		x = list(x)
		(x.insert(0,x.pop()))
		x = "".join(x)
	print(x)
	return True

count = 0

for i in range(2,1000000):
	if circular(i):
		count +=1

print(count)
