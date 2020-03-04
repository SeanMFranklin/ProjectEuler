import math

x = [2,3]
for i in range(1,2000000,2):
	k = 0
	for j in range(3,int(i**(1/2)+1)):
		if i%j == 0:
			break
		elif j==int(i**(1/2)):
			x.append(i)
			print(i)

print(sum(x))

				

# for i in range(2000000,2,-1):
	# k = 0
	# for j in range(i//2 + 1,1,-1):
		 # if i%j == 0:
			 # break
		 # elif j==2:
			 # print(i)
			 # break
