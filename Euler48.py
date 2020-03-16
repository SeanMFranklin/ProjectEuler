x = 0
for i in range(1, 1000):
    x += i**i
y = str(x)
print(y[len(y)-10:len(y)])
