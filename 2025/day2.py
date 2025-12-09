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


def check_num(n, loop_bound):
    test_value = str(n)
    for l in range(2, loop_bound):
        if len(test_value) % l == 0:
            tmp = len(test_value)//l
            ok = True
            for x in range(l-1):
                if test_value[x*tmp:(x+1)*tmp] != test_value[(x+1)*tmp:(x+2)*tmp]:
                    ok = False
                    break
            if ok:
                return True
    return False


def part1():
    acc = 0
    to_check = lin[0].split(',')
    for x in to_check:
        pair = x.split('-')
        if (len(pair[0]) % 2 == 0) or (len(pair[1]) % 2 == 0):
            for i in range(int(pair[0]), int(pair[1])+1):
                if check_num(i, 3):
                    acc += i
    return acc


def part2():
    acc = 0
    to_check = lin[0].split(',')
    for x in to_check:
        pair = x.split('-')
        for i in range(int(pair[0]), int(pair[1])+1):
            if check_num(i, len(str(i))+1):
                acc += i
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 2)]
start = time.time()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
