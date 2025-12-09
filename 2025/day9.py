import math
import re
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=128, typed=False)


def part1():
    max_size = 0
    for i1 in range(len(lin)):
        for i2 in range(i1, len(lin)):
            if i1 != i2:
                tmp = (abs(lin[i1][0]-lin[i2][0])+1) * \
                    (abs(lin[i1][1]-lin[i2][1])+1)
                if tmp > max_size:
                    max_size = tmp
    return max_size


def test_rect(p1, p2, pointlist) -> bool:
    if (not (p1 in pointlist)) and (p2 in pointlist):
        p1, p2 = p2, p1
    if (p1[0] == p2[0]):
        step = 1 if (p1[1] < p2[1]) else -1
        outside_dir = 1 if (not((p1[0]+1, p1[1]))in pointlist) else -1
        inside = False
        for i in range(p1[1], p2[1]+step, step):
            if (not ((p1[0], i) in pointlist)):
                if(not ((p1[0]-outside_dir, i-step) in pointlist)):
                    if not inside:
                        return False
                else:
                    inside = True
            else:
                inside = False
        return True
    if (p1[1] == p2[1]):
        step = 1 if (p1[0] < p2[0]) else -1
        outside_dir = 1 if (not((p1[0], p1[1]+1))in pointlist) else -1
        inside = False
        for i in range(p1[0], p2[0]+step, step):
            if (not ((i, p1[1]) in pointlist)):
                if (not ((i-step, p1[1]+outside_dir) in pointlist)):
                    if not inside:
                        return False
                else:
                    inside = True
            else:
                inside = False
        return True
    points = collections.deque([(p1[0], p1[1]), (p2[0], p1[1]), (p2[0], p2[1]), (p1[0], p2[1])])
    points.rotate(-points.index(min(points))-1)
    for i in range(-1, 3):
        Ok = True
        Ok = Ok and test_rect(points[i], points[i+1], pointlist)
        if not Ok:
            return False
    return True


def part2():
    pointlist = set()
    pointlist.add(lin[0])
    last = lin[0]
    for l in range(1, len(lin)):
        if lin[l][0] == last[0]:
            step = 1 if (lin[l][1] > last[1]) else -1
            for i in range(last[1], lin[l][1], step):
                pointlist.add((last[0], i+step))
                if i == lin[l][1]-step:
                    last = (last[0], i+step)

        if lin[l][1] == last[1]:
            step = 1 if (lin[l][0] > last[0]) else -1
            for i in range(last[0], lin[l][0], step):
                pointlist.add((i+step, last[1]))
                if i == lin[l][0]-step:
                    last = (i+step, last[1])

    if lin[0][0] == last[0]:
        step = 1 if (lin[0][1] > last[1]) else -1
        for i in range(last[1], lin[0][1], step):
            pointlist.add((last[0], i+step))
            if i == lin[0][1]-step:
                last = (last[0], i+step)

    if lin[0][1] == last[1]:
        step = 1 if (lin[0][0] > last[0]) else -1
        for i in range(last[0], lin[0][0], step):
            pointlist.add((i+step, last[1]))
            if i == lin[0][0]-step:
                last = (i+step, last[1])

    max_size = 0
    # test_rect([97579, 50266], [2448, 50249], pointlist)
    for i1 in range(len(lin)):
        for i2 in range(i1, len(lin)):
            if i1 != i2:
                tmp = (abs(lin[i1][0]-lin[i2][0])+1) * \
                    (abs(lin[i1][1]-lin[i2][1])+1)
                # print(f'testing {lin[i1]} - {lin[i2]}')
                if (tmp > max_size) and test_rect(lin[i1], lin[i2], pointlist):
                    max_size = tmp
                    print(f"current max size: {max_size}")

    return max_size


lin = [tuple(map(int, l.replace('\n', '').split(',')))
       for l in util.get_input(2025, 9)]
start = time.time()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
