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

numpad = ['789', '456', '123', ' 0A']
keypad = [' ^A', '<v>']
day = 21
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

start = time.time()
for i, l in enumerate(lin):
    a = int(l[0:3])

    # acc += a*len()

print('part 1: '+str(acc))
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
