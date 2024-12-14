import math
f = open('2024\input_day2', 'r')
lin = [l.replace('\n', '') for l in f.readlines()]
acc = 0
acc2 = 0
for l in lin:
    n = list(map(int, l.split(' ')))
    m = [n[i+1] - n[i] for i in range(len(n)-1)]
    if (max(m) <= 3) and (min(m) >= 1) or (min(m) >= -3) and (max(m) <= -1):
        acc += 1
print('part 1: '+str(acc))

for l in lin:
    n = list(map(int, l.split(' ')))
    safe = False
    for i in range(len(n)):
        n1 = n.copy()
        n1.pop(i)
        m = [n1[i+1] - n1[i] for i in range(len(n1)-1)]
        if (max(m) <= 3) and (min(m) >= 1) or (min(m) >= -3) and (max(m) <= -1):
            safe = True
            break
    if safe:
        acc2 += 1
print('part 2: '+str(acc2))
