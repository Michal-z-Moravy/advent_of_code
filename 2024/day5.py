import math
import re
f = open('2024\input_day5', 'r')
lin = [l.replace('\n', '') for l in f.readlines()]
acc = 0
acc2 = 0

mapping = dict()

section = 1
for l in lin:
    if l == '':
        section = 2
    else:
        if section == 1:
            a, b = list(map(int, l.split('|')))
            if not (a in mapping.keys()):
                mapping[a] = set([b])
            else:
                mapping[a].add(b)
        if section == 2:
            t = list(map(int, l.split(',')))
            ok = True
            try:
                for i in range(len(t)):
                    for j in range(i+1, len(t)):
                        if (not (t[j] in mapping[t[i]])) and (t[j] in mapping.keys()):
                            raise KeyError
            except:
                ok = False
            if ok:
                acc += t[(len(t)//2)]
            else:
                fix = dict()
                for i in t:
                    if i in mapping.keys():
                        tmp_counter = 0
                        for j in t:
                            if j in mapping[i]:
                                tmp_counter += 1
                        if tmp_counter in fix.keys():
                            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                        else:
                            fix[tmp_counter] = i
                s = sorted(fix.keys(), reverse=True)
                acc2 += fix[s[len(s)//2]]

print('part 1: '+str(acc))
print('part 2: '+str(acc2))
