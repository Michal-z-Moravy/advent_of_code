import math
import re
import util
import functools
import collections
import copy
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=128, typed=False)


def part1():
    acc = 0
    reading_ranges = True
    ranges = []
    for l in lin:
        if l == '':
            reading_ranges = False
            continue
        if reading_ranges:
            r1, r2 = l.split('-')
            ranges.append(range(int(r1), int(r2)+1))
        else:
            for r in ranges:
                tmp = int(l)
                if tmp in r:
                    acc += 1
                    break
    return acc


def part2():
    acc = 0
    tupleList = list()
    for l in lin:
        if l == '':
            break
        r1, r2 = l.split('-')
        tupleList.append((int(r1), int(r2)))
    tupleList = sorted(tupleList)
    prev_len = len(tupleList)
    while True:
        try:
            for tIndex1 in range(len(tupleList)):
                for tIndex2 in range(tIndex1+1, len(tupleList)):
                    if (((tupleList[tIndex1][1]+1) == tupleList[tIndex2][0]) or (tupleList[tIndex1][1] == tupleList[tIndex2][0])) or ((tupleList[tIndex2][0] < tupleList[tIndex1][1]) and (tupleList[tIndex2][0] >= tupleList[tIndex1][0])):
                        tupleList[tIndex1] = (
                            tupleList[tIndex1][0], tupleList[tIndex2][1])
                        tupleList.pop(tIndex2)
                        raise ZeroDivisionError
                    if (tupleList[tIndex2][0] >= tupleList[tIndex1][0]) and (tupleList[tIndex2][1] <= tupleList[tIndex1][1]):
                        tupleList.pop(tIndex2)
                        raise ZeroDivisionError
        except ZeroDivisionError:
            pass
        if len(tupleList) == prev_len:
            break
        prev_len = len(tupleList)

    print(tupleList)
    for tIndex1 in range(len(tupleList)):
        acc += tupleList[tIndex1][1]-tupleList[tIndex1][0]+1
    print(len(tupleList))
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 5)]
start = time.time()
print('part 1: '+str(part1()))

print('part 2: '+str(part2()))
end = time.time()
print(end - start)
