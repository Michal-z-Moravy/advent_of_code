import math
import re
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt


@functools.lru_cache(maxsize=None, typed=True)
def recurse_part2(node: str) -> int:
    if node.startswith('out-'):
        if node == 'out-11':
            return 1
        else:
            return 0
    else:
        return sum([recurse_part2(f'{n}-{"1" if((node[4]=="1")or(n=="fft")) else "0"}{"1" if((node[5]=="1")or(n=="dac")) else "0"}') for n in graph[node[:3]]])


@functools.lru_cache(maxsize=None, typed=True)
def recurse(node: str) -> int:
    if node == 'out':
        return 1
    else:
        return sum([recurse(n) for n in graph[node]])


def part1():
    return recurse("you")


def part2():
    return recurse_part2("svr-00")


lin = [l.replace('\n', '') for l in util.get_input(2025, 11)]
start = time.time()

graph = dict()
for l in lin:
    source, targets = l.split(": ")
    if not (source in graph):
        graph[source] = set(targets.split(" "))
    else:
        graph[source] = graph[source].union(set(targets.split(" ")))
    for t in targets.split(" "):
        if not (t in graph):
            graph[t] = set()

print('part 1: '+str(part1()))
print('part 2: '+str(part2()))
end = time.time()
print(end - start)
