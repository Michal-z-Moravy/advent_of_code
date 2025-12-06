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
    operators = [o for o in lin[-1] if o != " "]
    c = [0 if o == "+" else 1 for o in operators]
    for i in range(len(lin)-1):
        c_id = 0
        for x in lin[i].split(" "):
            if x != "":
                c[c_id] = (c[c_id]*int(x))if (operators[c_id]
                                              == '*')else (c[c_id]+int(x))
                c_id += 1
    return sum(c)


def part2():
    acc = 0
    transposed = []
    for x in range(len(lin[0])):
        tmp = []
        for y in range(len(lin)):
            tmp.append(lin[y][x])
        transposed.append(''.join(tmp))
    op = ''
    tmp = 0
    for t in transposed:
        if t == "     ":
            acc += tmp
            tmp = 0
            op = ''
            continue
        if t[-1] != " ":
            op = t[-1]
            tmp = 0 if (op == "+")else 1
        if op == "+":
            tmp += int(t[:len(t)-1])
        if op == "*":
            tmp *= int(t[:len(t)-1])
    return acc+tmp


day = 6
lin = [l.replace('\n', '') for l in util.get_input(day)]
start = time.time()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
