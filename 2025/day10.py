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


def merge_actions(a1, a2) -> tuple:
    tmp = list(a1)
    for i in a2:
        if i in tmp:
            tmp.pop(tmp.index(i))
        else:
            tmp.append(i)
    return tuple(sorted(tmp))


def process_line(i, target) -> int:
    j = 1
    tmp_actions = set(action_lists[i])
    while True:
        if target in tmp_actions:
            return j
        new_actions = set()
        tmp_actions_L = list(tmp_actions)
        for x in range(len(tmp_actions_L)):
            for y in range(x+1, len(tmp_actions_L)):
                new_actions.add(merge_actions(
                    tmp_actions_L[x], tmp_actions_L[y]))
        tmp_actions = tmp_actions.union(new_actions)
        j += 1


def part1():
    acc = 0
    for i in range(len(targets)):
        tmp = process_line(i, targets[i])
        out.write('steps: '+str(tmp)+' target: ' +
                  str(targets[i])+' input:'+lin[i]+'\n')
        acc += tmp
    return acc


def part2():
    acc = 0
    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 10)]
start = time.time()

out = open('output_day10', 'w')
targets = []
action_lists = []
joltages = []
for l in lin:
    tmp = l.split("] ")
    tmp_target = []
    for i in range(len(tmp[0][1:])):
        if tmp[0][1:][i] == '#':
            tmp_target.append(i)
    targets.append(tuple(tmp_target))
    tmp = tmp[1].split(" {")
    joltages.append(tuple(map(int, tmp[1][:len(tmp[1])-1].split(','))))
    action_lists.append(list(set(eval(
        '['+tmp[0].replace(" ", ",").replace('(', 'tuple([').replace(')', '])')+']'))))

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
out.close()
print(end - start)
