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


def get_dist(box1, box2):
    b1 = box1.split(',')
    b2 = box2.split(',')
    return math.sqrt((int(b1[0])-int(b2[0]))**2+(int(b1[1])-int(b2[1]))**2+(int(b1[2])-int(b2[2]))**2)


def part1_2():
    components = np.zeros(len(lin))
    component_id = 1
    dist_list = []
    for n1 in range(len(lin)):
        for n2 in range(n1, len(lin)):
            if n1 != n2:
                dist_list.append(((n1, n2), get_dist(lin[n1], lin[n2])))
    dist_list.sort(key=lambda index: index[1])
    # for i in range(10):
    #     print('('+str(dist_list[i][0][0])+')'+lin[dist_list[i][0][0]] + ' - ' + '('+str(dist_list[i][0][1])+')' + lin[dist_list[i][0][1]] + ' : '+str(dist_list[i][1]))
    target = 1000
    iterations = 0
    d = 0
    while d < (min(target, len(dist_list))):
        iterations += 1
        n1, n2 = dist_list[d][0]
        if (components[n1] != 0) and (components[n2] != 0):
            if components[n1] != components[n2]:
                replacement = (min(components[n1], components[n2]), max(
                    components[n1], components[n2]))
                for i in range(len(lin)):
                    if components[i] == replacement[1]:
                        components[i] = replacement[0]
        if (components[n1] == 0) and (components[n2] != 0):
            components[n1] = components[n2]
        if (components[n1] != 0) and (components[n2] == 0):
            components[n2] = components[n1]
        if (components[n1] == 0) and (components[n2] == 0):
            components[n1] = component_id
            components[n2] = component_id
            component_id += 1
        d += 1
    # print(components)
    # print('iterations: '+str(iterations))
    c = collections.Counter(components)
    mc = c.most_common(4)
    # print(c)
    acc = 1
    for mc_entry in mc:
        if mc_entry[0] != 0:
            acc *= mc_entry[1]

    print('part 1: '+str(acc))

    while d < len(dist_list):
        n1, n2 = dist_list[d][0]
        if (components[n1] != 0) and (components[n2] != 0):
            if components[n1] != components[n2]:
                replacement = (min(components[n1], components[n2]), max(
                    components[n1], components[n2]))
                for i in range(len(lin)):
                    if components[i] == replacement[1]:
                        components[i] = replacement[0]
        if (components[n1] == 0) and (components[n2] != 0):
            components[n1] = components[n2]
        if (components[n1] != 0) and (components[n2] == 0):
            components[n2] = components[n1]
        if (components[n1] == 0) and (components[n2] == 0):
            components[n1] = component_id
            components[n2] = component_id
            component_id += 1
        if components.sum() == len(lin):
            # print(lin[n1] + ' - ' + lin[n2])
            # print('components: '+str(components))
            print('part 2: ' +
                  str(int(lin[n1].split(',')[0])*int(lin[n2].split(',')[0])))
            break
        d += 1

    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 8)]
start = time.time()

part1_2()

end = time.time()
print(end - start)
