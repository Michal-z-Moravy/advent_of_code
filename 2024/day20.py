import math
import re
import requests
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=128, typed=False)

position_list = []


def explore():
    visited = set()
    visited.add((start_end_positions[0][0], start_end_positions[0][1]))
    position_list.append(
        (start_end_positions[0][0], start_end_positions[0][1], 0))
    queue = [(start_end_positions[0][0], start_end_positions[0][1], 0)]
    while len(queue) != 0:
        pos = queue.pop(0)
        for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (pos[0]+dir[0] >= 0) and (pos[1]+dir[1] >= 0) and (pos[0]+dir[0] <= bounds[0]) and (pos[1]+dir[1] <= bounds[1]) and (not ((pos[0]+dir[0], pos[1]+dir[1]) in visited)):
                if lin[pos[0]+dir[0]][pos[1]+dir[1]] in '.ES':
                    visited.add((pos[0]+dir[0], pos[1]+dir[1]))
                    queue.append((pos[0]+dir[0], pos[1]+dir[1], pos[2]+1))
                    position_list.append(
                        (pos[0]+dir[0], pos[1]+dir[1], pos[2]+1))


day = 20
lin = [l.replace('\n', '') for l in util.get_input(day)]
bounds = (len(lin), len(lin[0]))

acc = 0
acc2 = 0

start_end_positions = []
start = time.time()
for i, l in enumerate(lin):
    if 'S' in l:
        start_end_positions.append((i, l.index('S')))
    if 'E' in l:
        start_end_positions.append((i, l.index('E')))
explore()
cnt = collections.Counter()
for i in position_list:
    for j in position_list:
        if ((i[0] == j[0]) and (abs(i[1]-j[1]) == 2)) or ((i[1] == j[1]) and (abs(i[0]-j[0]) == 2)) or ((abs(i[1]-j[1]) == 1) and (abs(i[0]-j[0]) == 1)):
            if (i[2]-j[2]) > 2:
                cnt[(i[2]-j[2])-2] += 1
for k in cnt.keys():
    if k >= 100:
        acc += cnt[k]
print('part 1: '+str(acc))
# print('part 2: '+str(acc2))

end = time.time()
print(end - start)
