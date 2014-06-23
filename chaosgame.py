# This program draws a sierpinski triangle
#
#
#
from pylab import *
import pylab as pl
import math
import sys
import random 

iter = int(sys.argv[1])
deltaD = float(sys.argv[2])

x = [0, -1, 1]
y = [math.sqrt(3), 0, 0]
cx = 1.5
cy = 1.3

x.append(cx)
y.append(cy)
for i in range(iter):
	dice = random.randint(1,6)
	if (dice == 1 or dice == 2):
		cx = deltaD * (cx - 0)
		cy = deltaD * (cy - 0)
	if (dice == 3 or dice == 4):
		cx = deltaD * (cx - 2)
		cy = deltaD * (cy - 0)
	if (dice == 5 or dice == 6):
		cx = deltaD * (cx - 1)
		cy = deltaD * (cy - math.sqrt(3))
	x.append(cx)
	y.append(cy)

figure(1)
#pl.plot(x, y, 'go')
ax = subplot(1,1,1)
ax.plot(x, y, 'ro')
ax.set_xticks([])
ax.set_yticks([])
xlabel('x')
ylabel('y')
title('chaos game')
padding = [-2.5, 2.5, -2.5, 2.5] # [xmin. xmax, ymin, ymax]
plt.axis(padding)
pl.show()
