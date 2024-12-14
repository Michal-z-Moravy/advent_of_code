import math
import re
import util


def explore(o, p, d):
    global lin
    global acc2
    global visited_parts

    if not (o in visited_parts.keys()):
        visited_parts[o] = set()
    visited_parts[o].add(p)

    if d == 9:
        if lin[p[0]][p[1]] == '9':
            acc2 += 1
    else:
        for n in [(p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1)]:
            if (n[0] >= 0 and n[0] < len(lin)) and (n[1] >= 0 and n[1] < len(lin[0])):
                # and (not n in visited_parts[o]): #removed for part2
                if (int(lin[n[0]][n[1]]) == (int(lin[p[0]][p[1]])+1)):
                    explore(o, n, d+1)


day = 10
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

visited_parts = dict()
for y, l in enumerate(lin):
    for x, n in enumerate(l):
        if n == '0':
            explore((y, x), (y, x), 0)
            visited_parts.clear()

print('part 1: '+str(629))  # computed previously in part 1
print('part 2: '+str(acc2))
