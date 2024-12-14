import math
import re
f = open('2024\input_day4', 'r')
lin = [l.replace('\n', '') for l in f.readlines()]
acc = 0
acc2 = 0

to_test = 'XMAS'

for i in range(len(lin)):
    for j in range(len(lin[0])):
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
            if lin[i][j] == 'X':
                okay = True
                for n in range(4):
                    try:
                        if (lin[i+n*d[0]][j+n*d[1]] != to_test[n]) or ((i+n*d[0]) < 0) or ((j+n*d[1]) < 0) or ((i+n*d[0]) >= len(lin)) or ((j+n*d[1]) >= len(lin[0])):
                            okay = False
                    except:
                        okay = False
                if okay:
                    acc += 1

print('part 1: '+str(acc))


for i in range(len(lin)-2):
    for j in range(len(lin[0])-2):
        if (lin[i+1][j+1] == 'A') and (
            ((lin[i][j] == 'S') and (lin[i+2][j] == 'S') and (lin[i][j+2] == 'M') and (lin[i+2][j+2] == 'M')) or
            ((lin[i][j] == 'M') and (lin[i+2][j] == 'M') and (lin[i][j+2] == 'S') and (lin[i+2][j+2] == 'S')) or
            ((lin[i][j] == 'S') and (lin[i+2][j] == 'M') and (lin[i][j+2] == 'S') and (lin[i+2][j+2] == 'M')) or
            ((lin[i][j] == 'M') and (lin[i+2][j] == 'S') and (lin[i][j+2] == 'M') and (lin[i+2][j+2] == 'S'))):
            acc2 += 1
print('part 2: '+str(acc2))
