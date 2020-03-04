sumofpowers = 0
for i in range(1000000):
	powers = 0
	for j in str(i):
		powers+=int(j)**5
	if powers == i:
		sumofpowers+=powers
		print(powers)
print()
print(sumofpowers)
