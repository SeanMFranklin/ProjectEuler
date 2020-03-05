"""
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
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
