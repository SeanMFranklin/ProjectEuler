import Euler

start = 9
diff = 2
numerator = 3
denominator = 5
while numerator/denominator > .1:
    diff += 2
    for p in (start + diff, start + 2*diff, start + 3*diff, start + 4*diff):
        if Euler.is_prime(p):
            numerator += 1
    denominator += 4
    start += diff * 4
    if denominator % 101 == 0:
        print(start, denominator, numerator/denominator)


print(diff + 1)