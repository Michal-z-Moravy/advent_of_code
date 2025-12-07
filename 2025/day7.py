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


def part1_2():
    acc = 0
    beams = set()
    swap = set()
    visits = np.zeros([len(lin), len(lin[0])])
    beams.add((1, lin[0].index('S')))
    visits[1][lin[0].index('S')] = 1
    while True:
        for b in beams:
            if (b[0] < len(lin)-1):
                if (lin[b[0]][b[1]] == '.'):
                    swap.add((b[0]+1, b[1]))
                    visits[b[0]+1][b[1]] += visits[b[0]][b[1]]
                if (lin[b[0]][b[1]] == '^'):
                    acc += 1
                    swap.add((b[0]+1, b[1]-1))
                    swap.add((b[0]+1, b[1]+1))
                    visits[b[0]+1][b[1]-1] += visits[b[0]][b[1]]
                    visits[b[0]+1][b[1]+1] += visits[b[0]][b[1]]
        if len(swap) == 0:
            global part2_acc
            part2_acc = sum(visits[len(lin)-1])
            break
        swap, beams = beams, swap
        swap.clear()
    return (acc)


day = 7
lin = [l.replace('\n', '') for l in util.get_input(day)]
start = time.time()

part2_acc = 0

print('part 1: '+str(part1_2()))
print('part 2: '+str(part2_acc))
end = time.time()
print(end - start)
