"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, 
is the first Fibonacci number for which the last nine digits are 1-9 pandigital 
(contain all the digits 1 to 9, but not necessarily in order). 
And F2749, which contains 575 digits, 
is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits 
AND the last nine digits are 1-9 pandigital, find k."""
from itertools import permutations

possibilities = {''.join(i) for i in permutations('123456789', 9)}

a = 1
b = 1

count = 2
while True:
    b, a = a + b, b
    fib = str(b % 10**9)
    count += 1
    if fib[-9:] in possibilities:
        fib = str(b)
        if fib[:9] in possibilities:
            print(f"Answer: {count}")
            break
    if count % 10000 == 0:
        print(count//10000)
