import math
f = open('2024\input_day1', 'r')
lin = [l.replace('\n', '') for l in f.readlines()]
lin1, lin2 = [], []
for l in lin:
    tmp = l.split('   ')
    lin1.append(tmp[0])
    lin2.append(tmp[1])
lin1.sort()
lin2.sort()
sum = 0
for i in range(len(lin1)):
    sum += abs(int(lin1[i])-int(lin2[i]))
print('part 1: '+str(sum))
cnt = dict()
for l in lin2:
    if not (l in cnt):
        cnt[l] = 1
    else:
        cnt[l] += 1
sum = 0
for i in range(len(lin1)):
    if lin1[i] in cnt:
        sum += int(cnt[lin1[i]])*int(lin1[i])
print('part 2: '+str(sum))
