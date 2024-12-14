import math
import re
import requests
import util
import functools
import collections
import time


def expand_marks(m, pos):
    queue = [pos]
    while len(queue) != 0:
        p = queue.pop(0)
        if marks[p[0]][p[1]] is None:
            marks[p[0]][p[1]] = (m, offsets[m])
            if (p[1]-1 >= 0) and (marks[p[0]][p[1]-1] is None) and (lin[p[0]][p[1]-1] == m):
                queue.append((p[0], p[1]-1))
            if (p[1]+1 < len(lin[0])) and (marks[p[0]][p[1]+1] is None) and (lin[p[0]][p[1]+1] == m):
                queue.append((p[0], p[1]+1))
            if (p[0]-1 >= 0) and (marks[p[0]-1][p[1]] is None) and (lin[p[0]-1][p[1]] == m):
                queue.append((p[0]-1, p[1]))
            if (p[0]+1 < len(lin)) and (marks[p[0]+1][p[1]] is None) and (lin[p[0]+1][p[1]] == m):
                queue.append((p[0]+1, p[1]))


day = 12
lin = [l.replace('\n', '') for l in util.get_input(day)]

acc = 0
acc2 = 0

areas = collections.Counter()
perimeters = collections.Counter()
perimeters_2 = collections.Counter()
offsets = collections.Counter()

start = time.time()
for y in range(len(lin)):
    lin[y] = '#'+lin[y]+'#'
lin = ['#'*len(lin[0])]+lin+['#'*len(lin[0])]
marks = [[None for x in range(len(lin[0]))] for y in range(len(lin))]
for y in range(1, len(lin)-1):
    for x in range(1, len(lin[0])-1):
        region = lin[y][x]
        if marks[y][x] is None:
            offsets[region] += 1
            expand_marks(region, (y, x))
        areas[str(marks[y][x])] += 1
        if lin[y][x-1] != region:
            perimeters[str(marks[y][x])] += 1
            perimeters_2[str(marks[y][x])] += 1
            if (lin[y-1][x-1] != region) and (lin[y-1][x] == region):
                perimeters_2[str(marks[y][x])] -= 1
        if lin[y][x+1] != region:
            perimeters[str(marks[y][x])] += 1
            perimeters_2[str(marks[y][x])] += 1
            if (lin[y-1][x+1] != region) and (lin[y-1][x] == region):
                perimeters_2[str(marks[y][x])] -= 1
        if lin[y-1][x] != region:
            perimeters[str(marks[y][x])] += 1
            perimeters_2[str(marks[y][x])] += 1
            if (lin[y-1][x-1] != region) and (lin[y][x-1] == region):
                perimeters_2[str(marks[y][x])] -= 1
        if lin[y+1][x] != region:
            perimeters[str(marks[y][x])] += 1
            perimeters_2[str(marks[y][x])] += 1
            if (lin[y+1][x-1] != region) and (lin[y][x-1] == region):
                perimeters_2[str(marks[y][x])] -= 1

for k in areas.keys():
    acc += areas[k]*perimeters[k]


print('part 1: '+str(acc))

for k in areas.keys():
    acc2 += areas[k]*perimeters_2[k]

print('part 2: '+str(acc2))

end = time.time()
print(end - start)
