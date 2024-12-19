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


@functools.lru_cache(maxsize=128, typed=False)
def TryTowels(design):
    if design == '':
        return 1
    acc = 0
    for t in towels[design[0]]:
        if design[0:len(t)] == t:
            acc += TryTowels(design[len(t):])
    return acc


day = 19
lin = [l.replace('\n', '') for l in util.get_input(day)]

acc1 = 0
acc2 = 0

towels = {'w': set(), 'b': set(), 'u': set(), 'r': set(), 'g': set()}

start = time.time()
for i, l in enumerate(lin):
    if i == 0:
        for towel in l.split(', '):
            towels[towel[0]].add(towel)
    if i > 1:
        tmp = TryTowels(l)
        if tmp != 0:
            acc1 += 1
        acc2 += TryTowels(l)

print('part 1: '+str(acc1))
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
