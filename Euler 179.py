from math import sqrt


def num_of_divisors(n):
    res = 2
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            if n/i == i:
                res += 1
            else:
                res += 2
    return res


a = -1
b = -1
count = 0
for i in range(2, 1000000):
    b = num_of_divisors(i)
    # print(i,b)
    if a == b:
        count += 1
    a = b
    if i % 10001 == 0:
        print(f"{i/1e4}%")

print(count)
