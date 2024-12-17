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
    registers[0] = (registers[0])//(2**combo[operand])


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
    registers[1] = (registers[0])//(2**combo[operand])


def cdv(operand):
    combo = list(range(4))+list(registers)
    registers[2] = (registers[0])//(2**combo[operand])


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
            'Shit! Op='+str(program[program_counter])+' operand='+str(program[program_counter+1]))
    if program_counter == old_program_counter:
        program_counter += 2
print('part 1: '+','.join(map(str, output)))
# print('part 2: '+str(acc2))

for i in range(35184372088832, 281474976710656):
    A = i
    output.clear()
    # translated program
    while A != 0:
        B = ((A % 8) ^ 3)
        B = (B ^ (A//(2**B))) ^ 5
        if A == i:
            if str(B % 8) == '2':
                print(str(i) + ': ' + str(B) + ' ' + str(B % 8))
                raise Exception('a')
        A = A//(8)
        # output.append(B % 8)
    # break

    # registers[0] = i
    # program_counter = 0
    # output.clear()
    # while program_counter < len(program):
    #     old_program_counter = program_counter
    #     try:
    #         ops[program[program_counter]](program[program_counter+1])
    #     except:
    #         raise Exception(
    #             'Error! Op='+str(program[program_counter])+' operand='+str(program[program_counter+1]))
    #     if program_counter == old_program_counter:
    #         program_counter += 2
    # print(','.join(map(str, output)))
    # break

    # if ','.join(map(str, output)) == '2,4,1,3,7,5,4,2,0,3,1,5,5,5,3,0':
    #     print('part 2: '+str(i))
    #     break

end = time.time()
print(end - start)
