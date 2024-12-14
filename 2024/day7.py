import math
import re
import util
import itertools
from sympy.utilities.iterables import multiset_permutations

day = 7
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

tmp = -1
for l in lin:
    x = list(map(int, l.replace(':', '').split(' ')))
    target, start, nums = x[0], x[1], x[2:]
    com = itertools.combinations_with_replacement('*+', len(nums))
    for i in range(len(nums)+1):
        c = com.__next__()
        if ((i == 0) or (i == len(nums))):
            tmp = start
            for j in range(len(nums)):
                if c[j] == '+':
                    tmp += nums[j]
                else:
                    tmp *= nums[j]
            if tmp == target:
                acc += target
                break
        else:
            per = list(multiset_permutations(c))
            for p in per:
                tmp = start
                for j in range(len(nums)):
                    if p[j] == '+':
                        tmp += nums[j]
                    else:
                        tmp *= nums[j]
                if tmp == target:
                    acc += target
                    break
            if tmp == target:
                break

print('part 1: '+str(acc))

for l in lin:
    x = list(map(int, l.replace(':', '').split(' ')))
    target, start, nums = x[0], x[1], x[2:]
    com = itertools.combinations_with_replacement('*|+', len(nums))
    try:
        while True:
            c = com.__next__()
            per = list(multiset_permutations(c))
            for p in per:
                tmp = start
                for j in range(len(nums)):
                    if p[j] == '+':
                        tmp += nums[j]
                    elif p[j] == '*':
                        tmp *= nums[j]
                    else:
                        tmp = int(str(tmp)+str(nums[j]))
                if tmp == target:
                    acc2 += target
                    break
            if tmp == target:
                break
    except StopIteration:
        pass
print('part 2: '+str(acc2))
