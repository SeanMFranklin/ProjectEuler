def num_of_rectangle(n,m):
    return n*m*(n+1)*(m+1)/4

res = 0
n = 1
m = 1
dic = {(1,1):2000000-9}
for n in range(1,2000):
    for m in range(1,n):
        dic[(n,m)] = abs(2000000 - num_of_rectangle(n,m))

print(sorted(dic.items(),key = lambda x: x[1])[:10])