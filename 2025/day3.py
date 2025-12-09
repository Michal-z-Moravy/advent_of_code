import math
import re
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# @functools.lru_cache(maxsize=128, typed=False)


def recurse(l, start_index, temp_value):
    global line_values
    if l in line_values:
        return
    if len(temp_value) == 12:
        line_values[l] = temp_value
        return
    for digit in [str(y) for y in range(9, 0, -1)]:
        try:
            t = l.index(digit, start_index)
            if (t != len(l)) or (len(temp_value) == 11):
                recurse(l, t+1, temp_value+digit)
        except:
            pass


def test_line(l):
    for first_digit in [str(y) for y in range(9, 0, -1)]:
        try:
            t1 = l.index(first_digit)
            if t1 != len(l):
                for second_digit in [str(y) for y in range(9, 0, -1)]:
                    try:
                        t2 = l.index(second_digit, t1+1)
                        return (int(first_digit+second_digit))
                    except:
                        pass
        except:
            pass
    print(l)
    raise OverflowError


def part1():
    acc = 0
    for l in lin:
        acc += test_line(l)
    return acc


def part2():
    acc = 0
    global line_values
    for l in lin:
        recurse(l, 0, '')
        if l in line_values:
            acc += int(line_values[l])
        else:
            print('aaaaaaaaaaaaa')
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 3)]
start = time.time()

line_values = dict()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
