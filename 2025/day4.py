import math
import re
import util
import functools
import collections
import copy
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=128, typed=False)


def part1():
    acc = 0
    global lin2
    for y in range(1, len(lin)-1):
        for x in range(1, len(lin[0])-1):
            tmp = 0
            if lin[y][x] == '@':
                if lin[y-1][x-1] == '@':
                    tmp += 1
                if lin[y-1][x] == '@':
                    tmp += 1
                if lin[y-1][x+1] == '@':
                    tmp += 1
                if lin[y][x-1] == '@':
                    tmp += 1
                if lin[y][x+1] == '@':
                    tmp += 1
                if lin[y+1][x-1] == '@':
                    tmp += 1
                if lin[y+1][x] == '@':
                    tmp += 1
                if lin[y+1][x+1] == '@':
                    tmp += 1
                if tmp < 4:
                    acc += 1
                    lin2[y][x] = '.'
    return acc


def part2():
    acc = 0
    global lin2
    for y in range(1, len(lin2)-1):
        for x in range(1, len(lin2[0])-1):
            tmp = 0
            if lin2[y][x] == '@':
                if lin2[y-1][x-1] == '@':
                    tmp += 1
                if lin2[y-1][x] == '@':
                    tmp += 1
                if lin2[y-1][x+1] == '@':
                    tmp += 1
                if lin2[y][x-1] == '@':
                    tmp += 1
                if lin2[y][x+1] == '@':
                    tmp += 1
                if lin2[y+1][x-1] == '@':
                    tmp += 1
                if lin2[y+1][x] == '@':
                    tmp += 1
                if lin2[y+1][x+1] == '@':
                    tmp += 1
                if tmp < 4:
                    acc += 1
                    lin2[y][x] = '.'
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 4)]
lin2 = [list(l) for l in lin]
start = time.time()

total = part1()
print('part 1: '+str(total))

while True:
    tmp = part2()
    total += tmp
    if tmp == 0:
        break

print('part 2: '+str(total))
end = time.time()
print(end - start)
