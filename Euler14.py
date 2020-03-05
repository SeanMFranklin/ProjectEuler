""" Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


long_i = 0
longest = 0
for i in range(1, 1000000):
    x = i
    l = 0
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x+1
        l += 1
    if l > longest:
        longest = l
        long_i = i
        print(str(long_i) + ": " + str(longest))
print(str(long_i) + ": " + str(longest))
