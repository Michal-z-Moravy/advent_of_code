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
    val = 50
    acc = 0
    for l in lin:
        if l[0] == 'L':
            val -= int(l[1:])
        else:
            val += int(l[1:])
        val = val % 100
        if val == 0:
            acc += 1
    return acc


def part2():  # bruteforce - TODO: improve
    val = 50
    acc = 0
    for l in lin:
        mult = 1
        if l[0] == 'L':
            mult = -1
        for i in range(int(l[1:])):
            val += mult
            val = val % 100
            if val == 0:
                acc += 1
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 1)]
start = time.time()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
