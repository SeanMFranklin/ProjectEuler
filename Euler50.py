
def primecheck(x):
	for i in range(2,int(x**.5)+1):
		if x%i == 0:
			return False
	return True
	
primes = []

for i in range(2,100000):
	if primecheck(i):
		primes.append(i)

def findlargest():
	for i in range(550,2,-1):
		for j in range(len(primes)-i-1):
			if primecheck(sum(primes[j:j+i])) and sum(primes[j:j+i]) < 1000000:
				print(sum(primes[j:j+i]))
				print(primes[j:j+i])
				return(i)

print(findlargest())
