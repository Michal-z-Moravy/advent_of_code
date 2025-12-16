import math
import re
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=None, typed=False)


def test_line(req, dims)->bool:
    #TODO: implement proper shape fitting
    return True



lin = [l.replace('\n', '') for l in util.get_input(2025, 12)]
start = time.time()

shapes = [np.zeros((3,3), dtype=int) for _ in range(6)]
shape_sums = [0 for _ in range(6)]
for i in range(6):
    for j in range(3):
        for k in range(3):
            if lin[i*5+1+j][k]=='#':
                shapes[i][j][k] = 1
                shape_sums[i] += 1

checked = 0
for i in range(30,len(lin)):
    dimensions, requirements = lin[i].split(": ")
    dimensions = list(map(int, dimensions.split('x')))
    total_free_space = math.prod(dimensions)
    tmp = list(map(int, requirements.split(' ')))
    if sum([tmp[j]*shape_sums[j] for j in range(6)]) > total_free_space:
        continue
    if (dimensions[0]//3)*(dimensions[1]//3) < sum(tmp):
        if test_line(tmp, dimensions):
            checked += 1
    else:
        checked += 1

print('part 1: '+str(checked))
end = time.time()
print(end - start)
