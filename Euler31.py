from math import ceil
def sol1():
	count = 1
	for i in range(201):
		for j in range(ceil((201 - i ) / 2)):
			for k in range(ceil((201 - i - 2*j) / 5)):
				for l in range(ceil((201 - i - 2*j - 5*k) / 10)):
					for m in range(ceil((201 - i - 2*j - 5*k - 10*l) / 20)):
						for n in range(ceil((201 - i - 2*j - 5*k - 10*l - 20*m) / 50)):
							for o in range(ceil((201 - i - 2*j - 5*k - 10*l - 20*m - 50*n) / 100)):
								if i + 2*j + 5*k + 10*l + 20*m + 50*n + 100*o == 200:
										count +=1
		if i%10 == 0:
			print(str(i/201) + "%")
	print(count)

def sol2()
	ways = [0]*201
	ways[0] = 1
	coins = [1,2,5,10,20,50,100,200]
	for i in coins:
		for j in range(i,201):
			ways[j] += ways[j-i]
	print(ways[200])

def sol3():
	count = 0
	for i in range(0,201,2):
		for j in range(i,201,5):
			for k in range(j,201,10):
				for l in range(k,201,20):
					for m in range(l,201,50):
						for n in range(m,201,100):
							for o in range(n,201,200):
								count += 1
	print(count)