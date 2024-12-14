import math
import re
import requests
import util


def m_print(m):
    for n in m:
        print(n)
    print('--------------------------------------------')


lin = [l.replace('\n', '') for l in util.get_input(6)]
mark = [list(l) for l in lin]
acc = 0
acc2 = 0

pos = (-1, -1)
y = -1
x = -1
for l in lin:
    y += 1
    try:
        x = l.index('^')
        pos = (y, x)
        break
    except:
        pass

dir = (-1, 0)
try:
    while True:
        if dir == (-1, 0):
            for i in range(pos[0], -2, -1):
                if i == -1:
                    pos = (i, pos[1])
                    raise KeyError
                if (lin[i][pos[1]] != '#'):
                    mark[i][pos[1]] = 'x'
                else:
                    pos = (i+1, pos[1])
                    dir = (0, 1)
                    break
        if dir == (0, 1):
            for i in range(pos[1], len(lin[0])+1):
                if i == len(lin[0]):
                    pos = (pos[0], i)
                    raise KeyError
                if (lin[pos[0]][i] != '#'):
                    mark[pos[0]][i] = 'x'
                else:
                    pos = (pos[0], i-1)
                    dir = (1, 0)
                    break
        if dir == (1, 0):
            for i in range(pos[0], len(lin)+1):
                if i == len(lin):
                    pos = (i, pos[1])
                    raise KeyError
                if (lin[i][pos[1]] != '#'):
                    mark[i][pos[1]] = 'x'
                else:
                    pos = (i-1, pos[1])
                    dir = (0, -1)
                    break
        if dir == (0, -1):
            for i in range(pos[1], -2, -1):
                if i == -1:
                    pos = (pos[0], i)
                    raise KeyError
                if (lin[pos[0]][i] != '#'):
                    mark[pos[0]][i] = 'x'
                else:
                    pos = (pos[0], i+1)
                    dir = (-1, 0)
                    break
except Exception as ex:
    m_print(mark)
    pass

mark_positions = []
for i in range(len(mark)):
    for j in range(len(mark[0])):
        if mark[i][j] == 'x':
            acc += 1
            mark_positions.append((i, j))
print('part 1: '+str(acc))

for m in mark_positions:
    blocked = [list(l) for l in lin]
    blocked[m[0]][m[1]] = '#'
    pos = (y, x)
    dir = (-1, 0)
    visited = set()
    try:
        while True:
            if dir == (-1, 0):
                for i in range(pos[0], -2, -1):
                    if i == -1:
                        pos = (i, pos[1])
                        raise KeyError
                    if (blocked[i][pos[1]] == '#'):
                        pos = (i+1, pos[1])
                        if (pos, dir) in visited:
                            raise ZeroDivisionError
                        visited.add((pos, dir))
                        dir = (0, 1)
                        break
            if dir == (0, 1):
                for i in range(pos[1], len(lin[0])+1):
                    if i == len(lin[0]):
                        pos = (pos[0], i)
                        raise KeyError
                    if (blocked[pos[0]][i] == '#'):
                        pos = (pos[0], i-1)
                        if (pos, dir) in visited:
                            raise ZeroDivisionError
                        visited.add((pos, dir))
                        dir = (1, 0)
                        break
            if dir == (1, 0):
                for i in range(pos[0], len(lin)+1):
                    if i == len(lin):
                        pos = (i, pos[1])
                        raise KeyError
                    if (blocked[i][pos[1]] == '#'):
                        pos = (i-1, pos[1])
                        if (pos, dir) in visited:
                            raise ZeroDivisionError
                        visited.add((pos, dir))
                        dir = (0, -1)
                        break
            if dir == (0, -1):
                for i in range(pos[1], -2, -1):
                    if i == -1:
                        pos = (pos[0], i)
                        raise KeyError
                    if (blocked[pos[0]][i] == '#'):
                        pos = (pos[0], i+1)
                        if (pos, dir) in visited:
                            raise ZeroDivisionError
                        visited.add((pos, dir))
                        dir = (-1, 0)
                        break
    except Exception as ex:
        if str(type(ex)) == "<class 'ZeroDivisionError'>":
            acc2 += 1
        pass

print('part 2: '+str(acc2))
