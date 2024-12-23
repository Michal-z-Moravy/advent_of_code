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

def check_clique(to_check, stop_depth):
    if len(to_check) > 1:
        for i in range(len(to_check)):
            for j in range(i+1, len(to_check)):
                if matrix[to_check[i]][to_check[j]] == 0:
                    return
    tmp = tuple(sorted(to_check))
    if tmp in tiered_combinations[len(to_check)]:
        return
    tiered_combinations[len(to_check)].add(tmp)
    if len(to_check) == stop_depth-1:
        return
    for i in range(len(nodes)):
        if i not in to_check:
            check_clique(to_check+[i], stop_depth)

day = 23
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

nodes = set()

start = time.time()
for i, l in enumerate(lin):
    tmp = l.split('-')
    nodes.add(tmp[0])
    nodes.add(tmp[1])
nodes = list(nodes)
matrix = np.zeros((len(nodes), len(nodes)))
for i, l in enumerate(lin):
    indices = [nodes.index(k) for k in l.split('-')]
    matrix[indices[0]][indices[1]] = 1
    matrix[indices[1]][indices[0]] = 1

tiered_combinations = {1:set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set(), 11:set(), 12: set(), 13:set(), 14:set()}
for i in range(len(nodes)):
    check_clique([i], 4)
for c in tiered_combinations[3]:
    if (nodes[c[0]][0]=='t') or (nodes[c[1]][0]=='t') or (nodes[c[2]][0]=='t'):
        acc += 1
print('part 1: '+str(acc))

for c in tiered_combinations[3]:
    for i in range(len(nodes)):
        if i not in c:
            check_clique(list(c)+[i],14)

for i in range(14, 0, -1):
    if len(tiered_combinations[i]) > 0:
        for c in tiered_combinations[i]:
            tmp = [nodes[c1] for c1 in c]
            print('part 2: '+','.join(sorted(tmp)))
        break

end = time.time()
print(end - start)
