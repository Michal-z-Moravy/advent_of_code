import math
import re
import requests
import util
import functools
import collections
import time
import numpy as np


def int2(x):
    return int(x)+10000000000000


day = 13
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

start = time.time()
i = 0

for l in lin:
    i += 1
    if i == 1:
        A1 = list(map(int, l.replace('Button A: X+', '').split(', Y+')))
    elif i == 2:
        A2 = list(map(int, l.replace('Button B: X+', '').split(', Y+')))
    elif i == 3:
        b1 = list(map(int, l.replace('Prize: X=', '').split(', Y=')))
        b2 = list(map(int2, l.replace('Prize: X=', '').split(', Y=')))
    else:  # had to add a new line at the end of input file for this to work
        x = np.linalg.solve(
            np.array([[A1[0], A2[0]], [A1[1], A2[1]]]), np.array(b1))
        if (abs(x[0]-round(x[0])) < 0.0001) and (abs(x[1]-round(x[1])) < 0.0001):
            acc += 3*round(x[0])+round(x[1])
        x = np.linalg.solve(
            np.array([[A1[0], A2[0]], [A1[1], A2[1]]]), np.array(b2))
        if (abs(x[0]-round(x[0])) < 0.0001) and (abs(x[1]-round(x[1])) < 0.0001):
            acc2 += 3*round(x[0])+round(x[1])
        i = 0

print('part 1: '+str(int(acc)))
print('part 2: '+str(int(acc2)))

end = time.time()
print(end - start)
