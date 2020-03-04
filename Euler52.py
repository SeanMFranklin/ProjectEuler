x = 0
i =2
while x == 0:
	x1 = sorted(list(str(i)))
	x2 = sorted(list(str(i*2)))
	x3 = sorted(list(str(i*3)))
	x4 = sorted(list(str(i*4)))
	x5 = sorted(list(str(i*5)))
	x6 = sorted(list(str(i*6)))
	if x1 == x2 and x1 == x3 and x3 == x4 and x4 == x5 and x1 == x6:
		print(i)
		break
	i+=1
