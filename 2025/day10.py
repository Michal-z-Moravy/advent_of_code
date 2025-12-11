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
    tmp_action_costs = dict.fromkeys(set(action_lists[i]), 1)
    while True:
        if target in tmp_action_costs.keys():
            return tmp_action_costs[target]
        tmp_actions_L = list(tmp_action_costs.keys())
        for x in range(len(tmp_actions_L)):
            for y in range(x+1, len(tmp_actions_L)):
                action = merge_actions(tmp_actions_L[x], tmp_actions_L[y])
                cost = tmp_action_costs[tmp_actions_L[x]
                                        ]+tmp_action_costs[tmp_actions_L[y]]
                if (not (action in tmp_action_costs)) or (tmp_action_costs[action] > cost):
                    tmp_action_costs[action] = cost


def part1():
    acc = 0
    for i in range(len(targets)):
        acc += process_line(i, targets[i])
    return acc


def part2():
    acc = 0
    import pulp
    for i in range(len(joltages)):
        problem = pulp.LpProblem("Buttons_"+str(i), pulp.LpMinimize)
        x_nums = list(range(len(action_lists[i])))
        x = pulp.LpVariable.dicts(
            "Toggles_"+str(i), x_nums, lowBound=0, cat='Integer')
        problem += pulp.lpSum([x[j] for j in x_nums])
        m = np.zeros([len(x_nums), len(joltages[i])])
        for k in x_nums:
            for l in action_lists[i][k]:
                m[k][l] = 1
        for k in range(len(joltages[i])):
            problem += pulp.lpSum([x[j]*m[j][k]
                                  for j in x_nums]) == joltages[i][k]
        if pulp.LpStatus[problem.solve(pulp.PULP_CBC_CMD(msg=0))] == 'Optimal':
            acc += pulp.value(problem.objective)
        else:
            print("!!! ERROR !!!")

    return acc


lin = [l.replace('\n', '') for l in util.get_input(2025, 10)]
start = time.time()

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
print('part 2: '+str(int(part2())))
end = time.time()
print(end - start)
