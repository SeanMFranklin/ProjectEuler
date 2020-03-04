cubes = {}

for i in range(40000):
    cubed = ''.join(sorted(str(i**3)))
    if cubed not in cubes:
        cubes[cubed] = [i]
    else:
        cubes[cubed].append(i)

res = []
for j in cubes:
    if len(cubes[j]) == 5:
        res.append(cubes[j])

print(res)
flatres = [j for i in res for j in i]
print(flatres)
print(min(flatres)**3)