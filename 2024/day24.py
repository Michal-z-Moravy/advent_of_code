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

remapping = dict()

# @functools.lru_cache(maxsize=128, typed=False)
def process(l):
    tmp = l.split(' ')
    if (tmp[0] in values.keys()) and (tmp[2] in values.keys()):
        values[tmp[4]] = funcs[tmp[1]](values[tmp[0]], values[tmp[2]])
        return True
    return False

day = 24
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

section = 0
values = dict()
funcs = {'XOR': lambda x, y: x ^ y, 'AND': lambda x, y: x & y, 'OR': lambda x, y: x | y}
buffer = []

x,y = 0,0

start = time.time()
for i, l in enumerate(lin):
    if l == '':
        section += 1
        continue
    if section == 0:
        t,v = l.split(': ')
        values[t] = int(v)
        if t[0] == 'x':
            x += int(v)<<int(t[1:])
        else:
            y += int(v)<<int(t[1:])
    if section == 1:
        if not process(l):
            buffer.append(l)

while len(buffer) != 0:
    for i in buffer:
        if process(i):
            buffer.remove(i)

for k in values.keys():
    if k[0]=='z':
        acc += values[k]<<int(k[1:])
print('part 1: '+str(acc))

#print('part 2: '+str(acc2))

end = time.time()
print(end - start)
