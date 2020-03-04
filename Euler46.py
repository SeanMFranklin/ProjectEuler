from datetime import datetime
startTime = datetime.now()

def primecheck(x):
	for i in range(2,int(x**.5)+1):
		if x%i == 0:
			return False
	return True

oddcomp = []
for i in range(3,100000):
	if not primecheck(i) and i%2 == 1:
		oddcomp.append(i)

primes = []

for i in range(2,10000):
	if primecheck(i):
		primes.append(i)

def canbewritten(x):
	for i in primes[0:int(x/2)]:
		for j in range(1,int(x**.5)+2):
			if x == i+2*j**2:
				return (True, ("%d = %d + 2x%d^2" % (x,i,j)))
	return (False, ("\n%d can not be written as such\n" % x))

for i in oddcomp:
	(a,b) = canbewritten(i)
	if not a:
		print(b)
		break
	else:
		print(b)

print(datetime.now() - startTime)
