text = str(open("Euler13.txt", "rb").read())
x = []
y = 0
with open("Euler13.txt", "rb") as f:
    x = (f.read().splitlines())
print(x[1])
print(int(x[1]))
for i in x:
	y+=int(i)
y=str(y)
print(str(y[0:10]))
