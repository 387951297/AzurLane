from util import *
from const import const

yh = [[0] * 10 for i in range(10)]

for i in range(10):
    yh[i][0] = 1
    yh[i][i] = 1

for i in range(2, len(yh)):
    for j in range(1, i):
        yh[i][j] = yh[i-1][j-1] + yh[i-1][j]

for i in range(len(yh)):
    for j in range(i + 1):
        print("%4d" % yh[i][j], end = '')
    print()