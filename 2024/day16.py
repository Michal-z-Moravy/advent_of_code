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


def calc_score(current, dir):
    new_score = current[0]+1
    if current[1] != dir:
        new_score += 1000
    return new_score


day = 16
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

scores = []
start, end = (), ()
start_time = time.time()
for y, l in enumerate(lin):
    scores.append([(float('inf'), None)]*len(l))
    if 'E' in l:
        end = (y, l.index('E'))
    if 'S' in l:
        start = (y, l.index('S'))
scores[start[0]][start[1]] = (0, (0, 1, '>'))
queue = [start]
directions = [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]
while len(queue) != 0:
    position = queue.pop(0)
    for dir in directions:
        if lin[position[0]+dir[0]][position[1]+dir[1]] in '.E':
            tmp_score = calc_score(scores[position[0]][position[1]], dir)
            if tmp_score < scores[position[0]+dir[0]][position[1]+dir[1]][0]:
                scores[position[0]+dir[0]][position[1] +
                                           dir[1]] = (tmp_score, dir)
                queue.append((position[0]+dir[0], position[1]+dir[1]))

print('part 1: '+str(scores[end[0]][end[1]][0]))
# print('')
# for y, score_line in enumerate(scores):
#     for x, s in enumerate(score_line):
#         if lin[y][x] != '#':
#             print(str(s[0]).zfill(5)+s[1][2], end='')
#         else:
#             print(lin[y][x]*6, end='')
#     print('')

queue.append(end)
while len(queue) != 0:
    position = queue.pop(0)
    current_score = scores[position[0]][position[1]][0]
    for dir in directions:
        if scores[position[0]+dir[0]][position[1]+dir[1]][1] != None:
            if (scores[position[0]+dir[0]][position[1]+dir[1]][1][0:2] == (-dir[0], -dir[1])) and (position != end):
                # if (scores[position[0]+dir[0]][position[1]+dir[1]][0] < current_score):
                scores[position[0]+dir[0]][position[1] +
                                           dir[1]] = (current_score-1, 'O')
                # else:
                #     print('current '+scores[position[0]][position[1]][1][2]+': '+str(current_score) + ' prev'+scores[position[0]+dir[0]][position[1]+dir[1]][1][2]+': ' +
                #           str(scores[position[0]+dir[0]][position[1]+dir[1]][0]))
                #     scores[position[0]+dir[0]][position[1] + dir[1]
                #                                ] = (scores[position[0]+dir[0]][position[1] + dir[1]][0], '?')
    for dir in directions:
        if (scores[position[0]+dir[0]][position[1]+dir[1]][0] < current_score):
            queue.append((position[0]+dir[0], position[1]+dir[1]))
f2 = open('2024\\output_day16', 'w')
for y, score_line in enumerate(scores):
    for x, s in enumerate(score_line):
        if lin[y][x] != '#':
            if (s[1] == 'O') or (s[1] == '?'):
                f2.write(s[1])
            else:
                f2.write('.')
        else:
            f2.write(lin[y][x])
    f2.write('\n')
f2.close()
# print('part 2: '+str(acc2))
# For the part two I manually checked the output_day16, removed the paths that were too long and used ctrl-f to count occurrences of O
#
end_time = time.time()
print(end_time - start_time)
