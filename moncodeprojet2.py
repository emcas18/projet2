import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from scipy import interpolate
from BaselineRemoval import BaselineRemoval


my_file = open(r'C:\Users\emili\OneDrive\Bureau\Projet 2 optique\alcool 701.txt', "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

data = []
for i in content_list:
    x = i.split(',')
    data.append(x)

for j in data:
    if len(j) < 3:
        data.remove(j)


intensite = []
longueur = []
for k in range(0,1100):
    longueur.append(int(data[k][1]))
    intensite.append(int(float(data[k][2])))

plt.plot(longueur, intensite)
plt.show()
