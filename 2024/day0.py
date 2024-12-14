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

day = 0
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

start = time.time()
for l in lin:
    tmp = list(map(int, l.split(',')))

print('part 1: '+str(acc))
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
