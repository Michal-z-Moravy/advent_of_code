import math
import re
import requests
import util
import functools
import collections
import time


def expand_marks(field, m, pos):
    queue = [pos]
    while len(queue) != 0:
        p = queue.pop(0)
        if field[p[0]][p[1]] == 0:
            field[p[0]][p[1]] = offsets[m]
            if (p[1]-1 >= 0) and (0 == field[p[0]][p[1]-1]) and (lin[p[0]][p[1]-1] == m):
                queue.append((p[0], p[1]-1))
            if (p[1]+1 < len(lin[0])) and (0 == field[p[0]][p[1]+1]) and (lin[p[0]][p[1]+1] == m):
                queue.append((p[0], p[1]+1))
            if (p[0]-1 >= 0) and (0 == field[p[0]-1][p[1]]) and (lin[p[0]-1][p[1]] == m):
                queue.append((p[0]-1, p[1]))
            if (p[0]+1 < len(lin)) and (0 == field[p[0]+1][p[1]]) and (lin[p[0]+1][p[1]] == m):
                queue.append((p[0]+1, p[1]))


def init_marks(m, pos):
    field = [[0 for x in range(len(lin[0]))] for y in range(len(lin))]
    expand_marks(field, m, pos)
    marks[m] = field


day = 12
lin = [l.replace('\n', '') for l in util.get_input(day)]

# lin = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """.split('\n')
# lin.pop(-1)

acc = 0
acc2 = 0

areas = collections.Counter()
perimeters = collections.Counter()
perimeters_2 = collections.Counter()
offsets = collections.Counter()
marks = dict()

start = time.time()
for y in range(len(lin)):
    lin[y] = '#'+lin[y]+'#'
lin = ['#'*len(lin[0])]+lin+['#'*len(lin[0])]

for y in range(1, len(lin)-1):
    for x in range(1, len(lin[0])-1):
        region = lin[y][x]
        if not (region in marks.keys()):
            offsets[region] += 1
            init_marks(region, (y, x))
        else:
            if not marks[region][y][x]:
                offsets[region] += 1
                expand_marks(marks[region], region, (y, x))
        areas[region+str(marks[region][y][x])] += 1
        if lin[y][x-1] != region:
            perimeters[region+str(marks[region][y][x])] += 1
            perimeters_2[region+str(marks[region][y][x])] += 1
            if (lin[y-1][x-1] != region) and (lin[y-1][x] == region):
                perimeters_2[region+str(marks[region][y][x])] -= 1
        if lin[y][x+1] != region:
            perimeters[region+str(marks[region][y][x])] += 1
            perimeters_2[region+str(marks[region][y][x])] += 1
            if (lin[y-1][x+1] != region) and (lin[y-1][x] == region):
                perimeters_2[region+str(marks[region][y][x])] -= 1
        if lin[y-1][x] != region:
            perimeters[region+str(marks[region][y][x])] += 1
            perimeters_2[region+str(marks[region][y][x])] += 1
            if (lin[y-1][x-1] != region) and (lin[y][x-1] == region):
                perimeters_2[region+str(marks[region][y][x])] -= 1
        if lin[y+1][x] != region:
            perimeters[region+str(marks[region][y][x])] += 1
            perimeters_2[region+str(marks[region][y][x])] += 1
            if (lin[y+1][x-1] != region) and (lin[y][x-1] == region):
                perimeters_2[region+str(marks[region][y][x])] -= 1

for k in areas.keys():
    acc += areas[k]*perimeters[k]


print('part 1: '+str(acc))

for k in areas.keys():
    acc2 += areas[k]*perimeters_2[k]

print('part 2: '+str(acc2))

end = time.time()
print(end - start)
