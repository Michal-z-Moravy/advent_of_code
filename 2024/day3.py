import math
import re
f = open('2024\input_day3', 'r')
lin = [l.replace('\n', '') for l in f.readlines()]
acc = 0
acc2 = 0

for l in lin:
    x = re.findall('mul\(\d{1,3},\d{1,3}\)', l)
    for y in x:
        n = y[4:].strip(')').split(',')
        acc += int(n[0])*int(n[1])

print('part 1: '+str(acc))

res = []
buffer = []
enabled = True

for l in lin:
    x = re.findall('mul\(\d{1,3},\d{1,3}\)', l)
    tmp = l
    for y in x:
        tmp = tmp.split(y)
        res.append(tmp[0])
        if 'do()' in tmp[0]:
            enabled = True
        if 'don\'t()' in tmp[0]:
            enabled = False
        tmp = tmp[1]
        if enabled:
            n = y[4:].strip(')').split(',')
            acc2 += int(n[0])*int(n[1])
print('part 2: '+str(acc2))
