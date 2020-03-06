import csv
import matplotlib.pyplot as plt
import numpy as np

triangles = np.array([[int(j) for j in i] for i in csv.reader(open('p102_triangles.txt'))])
count = 0


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


for triangle in triangles:
    A, B, C = triangle[0:2], triangle[2:4], triangle[4:6]
    crosses = cross(A, B), cross(B, C), cross(C, A)
    if all(cross > 0 for cross in crosses) or all(cross < 0 for cross in crosses):
        count += 1
        print(f"Inside")
    else:
        print("Outside")
    X = np.append(triangle[::2], triangle[0])
    Y = np.append(triangle[1::2], triangle[1])
    plt.plot(X,Y)
    plt.scatter(0,0)
    plt.show()

print(count)
