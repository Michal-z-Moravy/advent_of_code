import math
import re
import util
import functools
import collections
import time
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from matplotlib import colors


day = 14
lin = [l.replace('\n', '') for l in util.get_input(day)]
acc = 1
acc2 = 0

bounds = [103, 101]
robots = []
start = time.time()
for l in lin:
    tmp = list(map(int, l.replace(' v=', ',').replace('p=', '').split(',')))
    robots.append([tmp[1], tmp[0], tmp[3], tmp[2]])

# create discrete colormap
cmap = colors.ListedColormap(['black', 'yellow'])
norm = colors.BoundaryNorm([0, 1, 2], cmap.N)

fig = plt.figure()
ax = fig.add_subplot(111)
data = np.zeros((bounds[0], bounds[1]))
im = ax.imshow(data, cmap=cmap, norm=norm)
plt.show(block=False)

for i in range(10000):
    data = np.zeros((bounds[0], bounds[1]))
    for r in robots:
        r[0], r[1] = (r[0]+r[2]) % bounds[0], (r[1]+r[3]) % bounds[1]
        data[r[0]][r[1]] = 1.5
    # By looking at the plot, some alignment happened at iterations 29 and 80
    # and also on further iterations where (i mod 103)=29 or (i mod 101)=80
    # solving the system of equations with chinese remainder theorem gives
    # 7857 which satisfies both equations. For some reason the plot does look
    # like christmas tree at this iteration.
    if (i % (10403) == 7857):
        plt.title('Iteration ' + str(i))
        im.set_data(data)
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(4)

quadrants = [0, 0, 0, 0]
for r in robots:
    if (r[0] == (bounds[0]//2)) or (r[1] == (bounds[1]//2)):
        continue
    if r[0] < (bounds[0]//2):
        index = 0
    elif (r[0] > (bounds[0]//2)):
        index = 1
    if r[1] < (bounds[1]//2):
        index += 0
    elif (r[1] > (bounds[1]//2)):
        index += 2
    quadrants[index] += 1
for q in quadrants:
    acc *= q

print('part 1: '+str(acc))
print('part 2: '+str(7857+1))  # The answer has 1 based index, I guess

end = time.time()
print(end - start)
