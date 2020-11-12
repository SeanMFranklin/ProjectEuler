from tqdm import tqdm
s_cache = {}

# Gather the first 90 fibonacci terms
fib_list = [1, 1]
for i in range(88):
    fib_list.append(fib_list[-1] + fib_list[-2])

def s(n):
    if n in s_cache:
        return s_cache[n]
    if n <= 9:
        s_cache[n] = n
        return n
    s_cache[n] = int(str(n%9) + '9'*(n//9))
    return s_cache[n]

def S(k):
    total = 0
    for i in range(1, fib_list[-1]):
        total += s(i)
        if i == k:
            yield total


res = 0
for f in tqdm(fib_list[1:]):
    res += S(f)
