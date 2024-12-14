import math
import re
import requests
import util

day = 9
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 0
acc2 = 0

pos = 0
for i in range(len(lin)):
    nums = list(map(int, lin[i]))
    end = len(nums)-1
    for j in range(len(nums)):
        if (j > end):
            break
        for k in range(nums[j]):
            if (j % 2 == 0):
                tmp = pos*(j//2)
                acc += tmp
            else:
                if (nums[end] == 0):
                    end -= 2
                tmp = pos*(end//2)
                acc += tmp
                nums[end] -= 1
            pos += 1
print('part 1: '+str(acc))

processed = set()
for i in range(len(lin)):
    nums = list(map(int, lin[i]))
    offset = [0 for j in range(len(nums))]
    cumsum = [0]
    for k in nums:
        cumsum.append(cumsum[-1]+k)
    start = 1
    n_copy = nums.copy()
    for j in range(len(nums)-1, -1, -2):
        for k in range(start, len(nums), 2):
            if k > j:
                break
            if (nums[j] <= nums[k]):
                acc2 += sum([(j//2)*n for n in range(cumsum[k] +
                            offset[k], cumsum[k]+offset[k]+nums[j])])
                nums[k] -= nums[j]
                offset[k] += nums[j]
                nums[j] = 0
                if nums[start] == 0:
                    start += 2
                processed.add(j)
                break

    for j in range(0, len(nums), 2):
        if (not j in processed):
            acc2 += sum([(j//2)*n for n in range(cumsum[j], cumsum[j]+nums[j])])
print('part 2: '+str(acc2))
