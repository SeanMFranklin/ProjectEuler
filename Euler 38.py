from itertools import permutations
possible = {''.join(i) for i in permutations('123456789',9)}
i = 200000
res = {}
print(possible)
while i > 0:
    number = ''
    for k in range(1,10):
        number = number + str(k*i)
        if number in possible:
            res[int(number)] = (i,k)
    i -= 1
    if i%500 == 0:
        print(f"{i/2000}%")
print(max(res))
print(res)