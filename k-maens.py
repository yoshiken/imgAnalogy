import numpy as np
import os
from sklearn.cluster import KMeans

dir = ('./kmeansres/')
file = os.listdir(dir)
datas = [[0 for i in range(400)] for j in range(400)]
filename = [0 for l in range(400)]
count = 0


for f in file:
    datas[count] = np.loadtxt(dir + f)
    filename[count] = f
    count += 1

kmeans_model = KMeans(n_clusters=4).fit(datas)

labels = kmeans_model.labels_

for label, data , fname in zip(labels, datas , filename):
        print ( fname + "," + str(label))
