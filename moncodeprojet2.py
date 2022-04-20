import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from scipy import interpolate
from BaselineRemoval import BaselineRemoval

def liste(nomdufichiertxt):
    my_file = open(r'C:\Users\emili\OneDrive\Bureau\Projet 2 optique\equipe biere\{}.txt'.format(nomdufichiertxt), "r")
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

    longueur = []
    intensite = []
    for k in range(200,1000):
        longueur.append(int(data[k][1]))
        intensite.append(int(float(data[k][2])))

    return longueur, intensite


def graphique(Data):
    longueur = liste(Data)[0]
    intensite = liste(Data)[1]
    plt.plot(longueur, intensite)
    plt.show()


def removeFLuo(Data):
        liste(Data)
        longueur = np.array(liste(Data)[0])
        intensite = np.array(liste(Data)[1])
        polynomial_degree=10 #only needed for Modpoly and IModPoly algorithm

        baseObj=BaselineRemoval(intensite)
        Modpoly_output=baseObj.ModPoly(polynomial_degree)
        Imodpoly_output=baseObj.IModPoly(polynomial_degree)
        Zhangfit_output=baseObj.ZhangFit()

        figure, axis = plt.subplots(2, 2)
  
        axis[0, 0].plot(longueur, intensite)
        axis[0, 0].set_title("Avec fluo")
  
        axis[0, 1].plot(longueur, Modpoly_output)
        axis[0, 1].set_title("Modpoly")
  
        axis[1, 0].plot(longueur, Imodpoly_output)
        axis[1, 0].set_title("Imodpoly")
  
        axis[1, 1].plot(longueur, Zhangfit_output)
        axis[1, 1].set_title("Zhangfit")

        plt.show()


def ratioeau(Data, Dataeau ='Sucre17'):
    longueur = liste(Data)[0]
    intensite = liste(Data)[1]
    intensiteeau = liste(Dataeau)[1]
    for i in intensite:
        for j in intensiteeau:
    ratio = intensite/intensiteeau
    plt.plot(longueur, ratio)
    plt.show()

ratioeau('coors1')
