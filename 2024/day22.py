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

day = 22
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

sequence_candidates = dict()
start = time.time()
for i, l in enumerate(lin):
    tmp = int(l)
    prev = tmp % 10
    sequence = []
    for j in range(2000):
        tmp = ((tmp << 6) ^ tmp) & 16777215
        tmp = ((tmp >> 5) ^ tmp) & 16777215
        tmp = ((tmp << 11) ^ tmp) & 16777215
        sequence.append((tmp % 10)-prev)
        prev = tmp % 10
        if j >= 3:
            s = tuple(sequence)
            if not (s in sequence_candidates):
                sequence_candidates[s] = [prev, set([i])]
            else:
                if not (i in sequence_candidates[s][1]):
                    sequence_candidates[s][0] += prev
                    sequence_candidates[s][1].add(i)
            sequence.pop(0)
    acc += tmp

print('part 1: '+str(acc))

for s in sequence_candidates.values():
    if s[0] > acc2:
        acc2 = s[0]
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
