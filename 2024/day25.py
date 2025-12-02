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

# @functools.lru_cache(maxsize=128, typed=False)

day = 25
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

keys=[]
locks=[]

buffer = []

start = time.time()
for i, l in enumerate(lin):
    if l != '':
        buffer.append(l)
    else:
        tmp = []
        for j in range(len(buffer[0])):
            tmp.append(len([k for k in buffer if k[j]=='#'])-1)
        if buffer[0][0]=='#':
            locks.append(tmp)
        else:
            keys.append(tmp)
        buffer.clear()

for k in keys:
    for l in locks:
        if all([(k[i]+l[i])<=5 for i in range(len(k))]):
            acc+=1

print('part 1: '+str(acc))
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
