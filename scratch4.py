def is_prime(n):
    """Returns T/F, whether n is prime or not"""
    if n & 1 == 0:
        return False
    d = 3
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 2
    return True

terms = [89, 271]
def sq_cub_rev_prime(n):
    k = terms[-1] + 1
    while n > len(terms):
        if is_prime(int(str(k ** 2)[::-1])):
            if is_prime(int(str(k ** 3)[::-1])):
                terms.append(k)
        k += 1
    print(terms)
    return terms[n - 1]

sq_cub_rev_prime(30)