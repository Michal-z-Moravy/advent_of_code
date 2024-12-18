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

bounds = (70, 70)


def explore(part):
    visited = set()
    visited.add((0, 0))
    queue = [(0, 0, 0)]
    while len(queue) != 0:
        pos = queue.pop(0)
        for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (pos[0]+dir[0] >= 0) and (pos[1]+dir[1] >= 0) and (pos[0]+dir[0] <= bounds[0]) and (pos[1]+dir[1] <= bounds[1]) and (not ((pos[0]+dir[0], pos[1]+dir[1]) in visited)):
                if grid[pos[0]+dir[0]][pos[1]+dir[1]]:
                    visited.add((pos[0]+dir[0], pos[1]+dir[1]))
                    queue.append((pos[0]+dir[0], pos[1]+dir[1], pos[2]+1))
                    if (pos[0]+dir[0] == bounds[0]) and (pos[1]+dir[1] == bounds[1]):
                        if part == 1:
                            print('part 1: '+str(pos[2]+1))
                        return True
    return False


day = 18
lin = [l.replace('\n', '') for l in util.get_input(day)]

grid = [[True for i in range(bounds[0]+1)] for j in range(bounds[1]+1)]
start = time.time()
for i, l in enumerate(lin):
    tmp = list(map(int, l.split(',')))
    grid[tmp[0]][tmp[1]] = False
    if i == 1023:
        explore(1)
    if i > 1023:
        if not explore(2):
            print('part 2: '+l)
            break

end = time.time()
print(end - start)
