import math
import re
import requests
import util
import collections

day = 11
lin = [l.replace('\n', '') for l in util.get_input(day)]

count_odd = collections.Counter()
count_even = collections.Counter()


def process(even):
    if even:
        count_target, count_source = count_odd, count_even
    else:
        count_target, count_source = count_even, count_odd
    count_target.clear()
    for k in count_source.keys():
        t = str(k)
        if k == 0:
            count_target[1] += count_source[k]
        elif len(t) % 2 == 1:
            count_target[k*2024] += count_source[k]
        else:
            count_target[int(t[0:len(t)//2])] += count_source[k]
            count_target[int(t[len(t)//2:])] += count_source[k]


for l in lin:
    nums = list(map(int, l.split(' ')))
    for n in nums:
        count_even[n] += 1

for i in range(25):
    process((i % 2) == 0)
print('part 1: '+str(sum([count_odd[k] for k in count_odd.keys()])))

for i in range(25, 75):
    process((i % 2) == 0)
print('part 2: '+str(sum([count_odd[k] for k in count_odd.keys()])))
