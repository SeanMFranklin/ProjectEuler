text = (open("Euler42.txt", "r"))				#Opens the file as text
words = text.read().split('","')
words = ([s.replace('"', '') for s in words])

count = 0
y = [1]
for i in range(2,100):
	y.append(y[i-2]+i)

for i in words:
	x = 0
	for j in i:
		x+= ord(j)-64
	if x in y:
		count += 1

print(words)
print(y)
print(count)
