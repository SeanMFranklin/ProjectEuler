"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital."""

from itertools import permutations

possibilities = [''.join(i) for i in permutations('123456789', 9)]

res = set()
for p in possibilities:
    for i in range(5,7):
        for j in range(1,i):
            a = int(p[:j])
            b = int(p[j:i])
            c = int(p[i:])
            if a * b == c:
                res.add(c)
                print(f"{a} * {b} = {c}")
print(f"\nAnswer: {sum(res)}")