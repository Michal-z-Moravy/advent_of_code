import math
import re
import requests
import util
import copy

day = 8
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc2 = 0
acc2 = 0

freq_map = dict()
for i in range(len(lin)):
    for j in range(len(lin[0])):
        freq = lin[i][j]
        if (freq != '.'):
            if freq in freq_map.keys():
                freq_map[freq].append((i, j))
            else:
                freq_map[freq] = [(i, j)]
antinodes = [list(l) for l in lin]
for f in freq_map.keys():
    f_list = freq_map[f]
    for i in range(len(f_list)):
        for j in range(i+1, len(f_list)):
            d = (f_list[i][0]-f_list[j][0], f_list[i][1]-f_list[j][1])
            done, mult = False, 0   #
            while not done:         # added in part 2
                done = True         #
                x, y = (f_list[i][0]+mult*d[0], f_list[i][1]+mult*d[1]
                        ), (f_list[j][0]-mult*d[0], f_list[j][1]-mult*d[1])
                if (x[0] >= 0 and x[0] < len(lin)) and (x[1] >= 0 and x[1] < len(lin[0])):
                    antinodes[x[0]][x[1]] = '#'
                    done = False
                if (y[0] >= 0 and y[0] < len(lin)) and (y[1] >= 0 and y[1] < len(lin[0])):
                    antinodes[y[0]][y[1]] = '#'
                    done = False
                mult += 1
for a in antinodes:
    acc2 += a.count('#')
print('part 1: '+str(348))  # previous result before adding part 2
print('part 2: '+str(acc2))
