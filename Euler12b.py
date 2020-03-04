# triangle = 1
# k = 1
# def numberofdivisors(x):
	# z=[]
	# y=0
	# for i in range(1,int(x/2)+1):
		# if x%i==0:
			# y+=1
	# return(y)
# numberofdivisors(30)

# for i in range(10000):
	# k+=1 
	# triangle += k
	# if numberofdivisors(triangle)>500:
		# print(triangle[i])
		# break
		
x=1
k = 0
y=1
while k<500:
	if x%y !=0:
		x*=y
		k+=1
	y+=1
print(x)
