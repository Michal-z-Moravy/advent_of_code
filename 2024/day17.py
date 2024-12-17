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


def adv(operand):
    combo = list(range(4))+list(registers)
    registers[0] = (registers[0]) >> combo[operand]


def bxl(operand):
    registers[1] = (registers[1]) ^ operand


def bst(operand):
    combo = list(range(4))+list(registers)
    registers[1] = combo[operand] % 8


def jnz(operand):
    if registers[0] != 0:
        global program_counter
        program_counter = operand


def bxc(operand):
    registers[1] = (registers[1]) ^ (registers[2])


def out(operand):
    combo = list(range(4))+list(registers)
    output.append(combo[operand] % 8)


def bdv(operand):
    combo = list(range(4))+list(registers)
    registers[1] = (registers[0]) >> combo[operand]


def cdv(operand):
    combo = list(range(4))+list(registers)
    registers[2] = (registers[0]) >> combo[operand]


day = 17
lin = [l.replace('\n', '') for l in util.get_input(day)]
registers = []
output = []
start = time.time()
for i, l in enumerate(lin):
    if i < 3:
        registers.append(int(l.replace('Register '+chr(ord('A')+i)+': ', '')))
    if i > 3:
        program = list(map(int, l.replace('Program: ', '').split(',')))
program_counter = 0
orig_registers = list(registers)
ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
while program_counter < len(program):
    old_program_counter = program_counter
    try:
        ops[program[program_counter]](program[program_counter+1])
    except:
        raise Exception(
            'Error! Op='+str(program[program_counter])+' operand='+str(program[program_counter+1]))
    if program_counter == old_program_counter:
        program_counter += 2
print('part 1: '+','.join(map(str, output)))

targets = [p ^ 5 for p in program[::-1]]
results = []

def explore(acc, targets):
    if len(targets) == 0:
        results.append(acc)
    else:
        for i in range(8):
            A = (acc << 3)+i
            B = i ^ 3
            B = (B ^ (A >> B)) % 8
            if B == targets[0]:
                explore(A, targets[1:])

explore(0, targets)
print('part 2: '+str(sorted(results)[0]))


#     #001 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000
#     #B = 011, 2**B = 8, A//8=A>>3, (B ^ (A//(2**B))) = 001 000 000 000 000 000 000 000 000 000 000 000 000 000 011,
#     #
#     #001 000 000 000 000 000 000 000 000 000 000 000 000 000 000 100
#     #B=111, B^(A>>7) = 001 000 000 000 000 000 000 000 000 000 000 00 111,^101 = 010
#     #
#     #001 000 000 000 000 000 000 000 000 000 000 000 000 000 010 100
#     #B=001, B^(A>>1) = 100 000 000 000 000 000 000 000 000 000 000 000 000 001 011 = 3
#     #
#     #
#     #110| 001| 001|...
#     # 5 |  6 |  0 |...


#     # translated program
#     while A != 0:
#         B = ((A % 8) ^ 3)
#         B = (B ^ (A>>B))
#         B = B^5
#         if A == i:
#             print(str(i) + ': ' + str(B) + ' ' + str(B % 8))
#         A = A//(8)
#         # output.append(B % 8)
#     # break

end = time.time()
print(end - start)
