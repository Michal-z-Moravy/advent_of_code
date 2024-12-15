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

def check(y,x,dir):
    if matrix[y][x] == '#':
        return [(y,x,False)]
    if matrix[y][x] == '.':
        return [(y,x,True)]
    if matrix[y][x] == '[':
        return [(y,x,True)]+check(y+dir,x,dir)+check(y+dir,x+1,dir)
    if matrix[y][x] == ']':
        return [(y,x,True)]+check(y+dir,x-1,dir)+check(y+dir,x,dir)

def move(m):
    if m == '<':
        if matrix[position[0]][position[1]-1] == '.':
            matrix[position[0]][position[1]-1:position[1]+1] = ['@','.']
            position[1] -= 1
            return
        if matrix[position[0]][position[1]-1] == 'O':
            for i in range(position[1]-2, -1, -1):
                if matrix[position[0]][i] == '#':
                    return
                if matrix[position[0]][i] == '.':
                    matrix[position[0]][i] = 'O'
                    matrix[position[0]][position[1]-1:position[1]+1] = ['@','.']
                    position[1] -= 1
                    return
        if matrix[position[0]][position[1]-1] == ']':
            boxes = 0
            for i in range(position[1]-2, -1, -1):
                if matrix[position[0]][i] == '#':
                    return
                if matrix[position[0]][i] == '[':
                    boxes += 1
                if matrix[position[0]][i] == '.':
                    matrix[position[0]][i:i+2*boxes] = ['[',']']*boxes
                    matrix[position[0]][position[1]-1:position[1]+1] = ['@','.']
                    position[1] -= 1
                    return
    if m == '>':
        if matrix[position[0]][position[1]+1] == '.':
            matrix[position[0]][position[1]:position[1]+2] = ['.','@']
            position[1] += 1
            return
        if matrix[position[0]][position[1]+1] == 'O':
            for i in range(position[1]+2, len(matrix[position[0]])):
                if matrix[position[0]][i] == '#':
                    return
                if matrix[position[0]][i] == '.':
                    matrix[position[0]][i] = 'O'
                    matrix[position[0]][position[1]:position[1]+2] = ['.','@']
                    position[1] += 1
                    return
        if matrix[position[0]][position[1]+1] == '[':
            boxes = 0
            for i in range(position[1]+2, len(matrix[position[0]])):
                if matrix[position[0]][i] == '#':
                    return
                if matrix[position[0]][i] == ']':
                    boxes += 1
                if matrix[position[0]][i] == '.':
                    matrix[position[0]][position[1]+2:position[1]+2+2*boxes] = ['[',']']*boxes
                    matrix[position[0]][position[1]:position[1]+2] = ['.','@']
                    position[1] += 1
                    return
    if m == '^':
        if matrix[position[0]-1][position[1]] == '.':
            matrix[position[0]][position[1]],matrix[position[0]-1][position[1]] = '.','@'
            position[0] -= 1
            return
        if matrix[position[0]-1][position[1]] == 'O':
            for i in range(position[0]-2, -1, -1):
                if matrix[i][position[1]] == '#':
                    return
                if matrix[i][position[1]] == '.':
                    matrix[i][position[1]] = 'O'
                    matrix[position[0]][position[1]],matrix[position[0]-1][position[1]] = '.','@'
                    position[0] -= 1
                    return
        if matrix[position[0]-1][position[1]] in '[]':
            res = sorted(list(set(check(position[0]-1,position[1],-1))))
            if all([r[2] for r in res]):
                for r in res:
                    matrix[r[0]][r[1]],matrix[r[0]+1][r[1]] = matrix[r[0]+1][r[1]],matrix[r[0]][r[1]]
                matrix[position[0]][position[1]],matrix[position[0]-1][position[1]] = '.','@'
                position[0] -= 1
            return
    if m == 'v':
        if matrix[position[0]+1][position[1]] == '.':
            matrix[position[0]][position[1]],matrix[position[0]+1][position[1]] = '.','@'
            position[0] += 1
            return
        if matrix[position[0]+1][position[1]] == 'O':
            for i in range(position[0]+2, len(matrix)):
                if matrix[i][position[1]] == '#':
                    return
                if matrix[i][position[1]] == '.':
                    matrix[i][position[1]] = 'O'
                    matrix[position[0]][position[1]],matrix[position[0]+1][position[1]] = '.','@'
                    position[0] += 1
                    return
        if matrix[position[0]+1][position[1]] in '[]':
            res = sorted(list(set(check(position[0]+1,position[1],1))), reverse=True)
            if all([r[2] for r in res]):
                for r in res:
                    matrix[r[0]][r[1]],matrix[r[0]-1][r[1]] = matrix[r[0]-1][r[1]],matrix[r[0]][r[1]]
                matrix[position[0]][position[1]],matrix[position[0]+1][position[1]] = '.','@'
                position[0] += 1
            return
    return

day = 15
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0
section = 0
matrix = []
position = [-1, -1]
start = time.time()
for i,l in enumerate(lin):
    if l == '':
        for y in range(len(matrix)):
            print(''.join(matrix[y]))
        print('')
        section += 1
        continue
    if section == 0:
        matrix.append(list(l))
        if '@' in l:
            position[0] = i
            position[1] = l.index('@')
    if section == 1:
        for m in l:
            move(m)

for y in range(len(matrix)):
    print(''.join(matrix[y]))
    for x in range(len(matrix[0])):
        if matrix[y][x] == 'O':
            acc += 100*y+x
print('part 1: '+str(acc))

section = 0
matrix = []
control_sums = [0,0]
position = [-1, -1]
for i,l in enumerate(lin):
    if l == '':
        section += 1
        for m in matrix:
            control_sums[0] += m.count('[')
            control_sums[1] += m.count(']')
        continue
    if section == 0:
        row = []
        for x in l:
            if x == '#':
                row += ['#','#']
            if x == '.':
                row += ['.','.']
            if x == '@':
                row += ['@','.']
            if x == 'O':
                row += ['[',']']
        matrix.append(row)
        if '@' in l:
            position[0] = i
            position[1] = row.index('@')
    if section == 1:
        for j, m in enumerate(l):
            move(m)
            sums = [0,0]
            for mat in matrix:
                sums[0] += mat.count('[')
                sums[1] += mat.count(']')
            if sums != control_sums:
                raise Exception('Something wrong at '+str(i)+':'+str(j) + ' ' + m)

for y in range(len(matrix)):
    print(''.join(matrix[y]))
    for x in range(len(matrix[0])):
        if matrix[y][x] == '[':
            acc2 += 100*y+x
print('part 2: '+str(acc2))

end = time.time()
print(end - start)
