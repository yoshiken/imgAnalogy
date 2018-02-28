import numpy as np
import matplotlib.pyplot as plt
import os

y = []
x = []
c = 0
for line in open('hogehoge', 'r'):
    line = line.replace('\n','')
    line = line.replace('\r','')
    x.append(line)
    y.append(c)
    c += 1
plt.xlabel('使用データ')
plt.ylabel('類似度')
plt.yticks( [0, 100, 200, 300, 400, 500] )
plt.plot(y, x)
plt.show()
