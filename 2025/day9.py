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


def test_rect(p1, p2, pointlist, shell) -> bool:
    if (not (p1 in pointlist)) and (p2 in pointlist):
        p1, p2 = p2, p1
    if (p1[0] == p2[0]):
        step = 1 if (p1[1] < p2[1]) else -1
        for i in range(p1[1], p2[1]+step, step):
            if (not ((p1[0], i) in pointlist)) and ((p1[0], i) in shell):
                return False
        return True
    if (p1[1] == p2[1]):
        step = 1 if (p1[0] < p2[0]) else -1
        for i in range(p1[0], p2[0]+step, step):
            if (not ((i, p1[1]) in pointlist)) and (((i, p1[1]) in shell)):
                return False
        return True
    points = [(p1[0], p1[1]), (p2[0], p1[1]), (p2[0], p2[1]), (p1[0], p2[1])]
    for i in range(-1, 3):
        if not test_rect(points[i], points[i+1], pointlist, shell):
            return False
    return True


def part2():
    pointlist = set()
    shell1, shell2 = set(), set()
    pointlist.add(lin[0])
    last = lin[0]
    for l in range(1, len(lin)):
        if lin[l][0] == last[0]:
            step = 1 if (lin[l][1] > last[1]) else -1
            for i in range(last[1], lin[l][1], step):
                pointlist.add((last[0], i+step))
                if not ((last[0]+step, i+step) in pointlist):
                    shell1.add((last[0]+step, i+step))
                # if not ((last[0]-step, i+step) in pointlist):
                #     shell2.add((last[0]-step, i+step))
                if i == lin[l][1]-step:
                    last = (last[0], i+step)

        if lin[l][1] == last[1]:
            step = 1 if (lin[l][0] > last[0]) else -1
            for i in range(last[0], lin[l][0], step):
                pointlist.add((i+step, last[1]))
                # if not ((i+step, last[1]+step) in pointlist):
                #     shell2.add((i+step, last[1]+step))
                if not ((i+step, last[1]-step) in pointlist):
                    shell1.add((i+step, last[1]-step))
                if i == lin[l][0]-step:
                    last = (i+step, last[1])

    if lin[0][0] == last[0]:
        step = 1 if (lin[0][1] > last[1]) else -1
        for i in range(last[1], lin[0][1], step):
            pointlist.add((last[0], i+step))
            if not ((last[0]+step, i+step) in pointlist):
                shell1.add((last[0]+step, i+step))
            # if not ((last[0]-step, i+step) in pointlist):
            #     shell2.add((last[0]-step, i+step))
            if i == lin[0][1]-step:
                last = (last[0], i+step)

    if lin[0][1] == last[1]:
        step = 1 if (lin[0][0] > last[0]) else -1
        for i in range(last[0], lin[0][0], step):
            pointlist.add((i+step, last[1]))
            # if not ((i+step, last[1]+step) in pointlist):
            #     shell2.add((i+step, last[1]+step))
            if not ((i+step, last[1]-step) in pointlist):
                shell1.add((i+step, last[1]-step))
            if i == lin[0][0]-step:
                last = (i+step, last[1])

    max_size = 0
    special_points = []
    prev = lin[0]
    for l in lin:
        if l == prev:
            continue
        if math.sqrt((prev[0]-l[0])**2+(prev[1]-l[1])**2) > 50000:
            special_points.append(prev)
            special_points.append(l)
        prev = l
    if math.sqrt((prev[0]-lin[0][0])**2+(prev[1]-lin[0][1])**2) > 50000:
        special_points.append(prev)
        special_points.append(lin[0])

    # plt.plot(ndarr[0], ndarr[1])

    # ndarr2 = np.zeros([2, len(shell1)])
    # shell1_l = list(shell1)
    # for i in range(len(shell1)):
    #     ndarr2[0][i] = shell1_l[i][0]
    #     ndarr2[1][i] = shell1_l[i][1]
    # plt.scatter(ndarr2[0], ndarr2[1])
    # plt.show()

    print(special_points)

    for i1 in special_points:
        for i2 in lin:
            if i1 != i2:
                tmp = (abs(i1[0]-i2[0])+1) * (abs(i1[1]-i2[1])+1)
                if (tmp > max_size) and test_rect(i1, i2, pointlist, shell1):
                    max_size = tmp
                    # plt.plot(ndarr[0], ndarr[1])
                    # plt.plot([i1[0], i1[0], i2[0], i2[0], i1[0]],
                    #          [-i1[1], -i2[1], -i2[1], -i1[1], -i1[1]])
                    # plt.show()
                    print(f"current max size: {max_size}")

    return max_size


lin = [tuple(map(int, l.replace('\n', '').split(',')))
       for l in util.get_input(2025, 9)]
start = time.time()

ndarr = np.zeros([2, len(lin)+1])
for i in range(-1, len(lin)):
    ndarr[0][i+1] = lin[i][0]
    ndarr[1][i+1] = -lin[i][1]

# fig = plt.figure()
# # creating a timer object and setting an interval of 3000 milliseconds
# timer = fig.canvas.new_timer(interval=3000)
# timer.add_callback(close_event)
# # print(ndarr)
# plt.plot(ndarr[0], ndarr[1])
# # timer.start()
# plt.show()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
