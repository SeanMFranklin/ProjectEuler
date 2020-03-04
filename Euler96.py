import numpy as np
import time

def deductive(sudo):
    flag = 2
    A = [[[]for i in range(9)] for j in range(9)]
    while flag > 0:
        flag -= 1
        for j in range(9):
            for i in range(9):
                if sudo[j, i] == 0:
                    xmin, ymin = (i // 3) * 3, (j // 3) * 3
                    s = [k for k in range(1, 10) if
                         k not in sudo[j, :] and k not in sudo[:, i] and k not in sudo[ymin:ymin + 3, xmin:xmin + 3]]
                    A[j][i] = s
                    if len(s) == 1:
                        flag += 1
                        sudo[j, i] = s[0]
        for j in range(9):
            for i in range(9):
                if sudo[j, i] == 0:
                    xmin, ymin = (i // 3) * 3, (j // 3) * 3
                    s = [k for k in range(1, 10) if
                         k not in sudo[j, :] and k not in sudo[:, i] and k not in sudo[ymin:ymin + 3, xmin:xmin + 3]]
                    A[j][i] = s
                    if len(s) == 1:
                        flag += 1
                        sudo[j, i] = s[0]
                    for k in range(1, 9):
                        if np.int.count(sudo[j, :],k) == 1 or np.int.count(sudo[:, i],k) == 1 or np.int.count(sudo[ymin:ymin + 3, xmin:xmin + 3],k):
                            sudo[j, i] = k
                            flag += 1

    return sudo


def deductive(sudo):
    if 0 not in sudo[:, :]:
        return True
    bpos = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for i in range(9)] for j in range(9)]
    flag = -1
    while flag < 1:
        flag += 1
        flag = max(0,flag)
        for y in range(9):
            for x in range(9):
                xmin, ymin = (x // 3) * 3, (y // 3) * 3
                if sudo[y, x] != 0:
                    bpos[y][x] = {sudo[y, x]}
                else:
                    bpos[y][x] = {i for i in bpos[y][x] if
                              i not in sudo[y, :] and
                              i not in sudo[:, x] and
                              i not in sudo[ymin:ymin + 3, xmin:xmin + 3]}
                    if len(bpos[y][x]) == 1:
                        sudo[y, x] = list(bpos[y][x])[0]
                        #                     print(sudo)
                        #                     print(x,y,sudo[y,x])
                        flag -= 1
        for y in range(9):
            for x in range(9):
                if sudo[y,x] == 0:
                    xmin, ymin = (x // 3) * 3, (y // 3) * 3
                    col = [k for j in range(9) for k in bpos[j][x]]
                    row = [k for i in range(9) for k in bpos[y][i]]
                    box = [k for i in range(xmin,xmin+3) for j in range(ymin,ymin + 3) for k in bpos[j][i]]
                    for num in bpos[y][x]:
                        if col.count(num) == 1 or row.count(num) == 1 or box.count(num) == 1:
                            sudo[y,x] = num
                            flag -= 1
#                 Hidden Twins

#                   Naked Twins
                if sudo[y, x] == 0:
                    s = bpos[y][x]
                    if len(s) == 2:
                        colp = [bpos[j][x] for j in range(9)]
                        if colp.count(s) == 2:
                            for j in range(9):
                                if bpos[j][x] != s:
                                    bpos[j][x] = bpos[j][x].difference(s)
                            # print([bpos[j][x] for j in range(9)])
                            # print()
                    rowp = [bpos[y][i] for i in range(9)]
                    for s in rowp:
                        if len(s) == 2:
                            if rowp.count(s) == 2:
                                for i in range(9):
                                    if bpos[y][i] != s:
                                        bpos[y][i] = bpos[y][i].difference(s)
                    boxp = [bpos[j][i] for i in range(xmin, xmin + 3) for j in range(ymin, ymin + 3)]
                    for s in boxp:
                        if len(s) == 2:
                            if boxp.count(s) == 2:
                                for i in range(xmin, xmin + 3):
                                    for j in range(ymin, ymin + 3):
                                        if bpos[j][i] != s:
                                            bpos[j][i] = bpos[j][i].difference(s)
    return bpos


def solver(sudo, bpos):
    if not (0 in sudo[:, :]):
        return True
    y, x = np.where(sudo == 0)[0][0], np.where(sudo == 0)[1][0]
    xmin, ymin = (x // 3) * 3, (y // 3) * 3
    s = {i for i in bpos[y][x] if
         i not in sudo[y, :] and i not in sudo[:, x] and i not in sudo[ymin:ymin + 3, xmin:xmin + 3]}
    for i in s:
        sudo[y][x] = i
        if solver(sudo, bpos):
            return True
        sudo[y][x] = 0


sum = 0
f = open('p096_sudoku.txt', 'r')
start = time.time()
for i in range(50):
    print(f.readline())
    A = f.readlines(81)
    A = np.array([[int(j) for j in list(i.replace('\n', ''))] for i in A])
    print(A, '\n')
    old = np.sum(A == 0)
    bpos = deductive(A)
    print('Deductive found %d answers.\n' % (old - np.sum(A == 0)))
    # print('\n',A,)
    # for l in bpos:
    #     print(l)
    # print()
    solver(A,bpos)
    print(A, '\n\n')
    sum += A[0][0] * 100 + A[0][1] * 10 + A[0][2]
print("Solution:", sum)
print("Time: ",time.time() - start)
