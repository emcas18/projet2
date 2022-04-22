import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from scipy import interpolate
from BaselineRemoval import BaselineRemoval
import pandas as pd

def liste(nomdufichiertxt):
    my_file = open(r'C:\Users\emili\OneDrive\Bureau\Data\projet 2\Projet2 Emilie\{}.txt'.format(nomdufichiertxt), "r")
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
    for k in range(0,len(data)-1):
        longueur.append(int(float(data[k][1])))
        intensite.append(int(float(data[k][2])))
    #plt.plot(longueur, intensite[::-1])
    #plt.xlim(max(longueur), 200)
    #plt.ylim(60000, 120000)
    #plt.show()
    return longueur, intensite


def removeFLuo(Data):
        liste(Data)
        longueur = np.array(liste(Data)[0])
        intensite = np.array(liste(Data)[1])
        polynomial_degree=10 #only needed for Modpoly and IModPoly algorithm

        baseObj=BaselineRemoval(intensite)
        Modpoly_output=baseObj.ModPoly(polynomial_degree)
        Imodpoly_output=baseObj.IModPoly(polynomial_degree)
        Zhangfit_output=baseObj.ZhangFit()

        #figure, axis = plt.subplots(2, 2)

  
        #axis[0, 0].plot(longueur, intensite[::-1])
        #axis[0, 0].set_title("Avec fluo")
        #axis[0, 0].set_xlim(max(longueur), 200)
        #axis[0, 0].set_ylim(63000, 1000000)
  
        #axis[0, 1].plot(longueur, Modpoly_output[::-1])
        #axis[0, 1].set_title("Modpoly")
        #axis[0, 1].set_xlim(max(longueur), 200)
        #axis[0, 1].set_ylim(-10000, 200000)

  
        #axis[1, 0].plot(longueur, Imodpoly_output[::-1])
        #axis[1, 0].set_title("Imodpoly")
        #axis[1, 0].set_xlim(max(longueur), 200)
        #axis[1, 0].set_ylim(0, 200000)
  
        #axis[1, 1].plot(longueur, Zhangfit_output[::-1])
        #axis[1, 1].set_title("Zhangfit")
        #axis[1, 1].set_xlim(max(longueur), 200)
        #axis[1, 1].set_ylim(0, 500000)

        #plt.show()
        return longueur, Modpoly_output[::-1]

def ratioeau(Data, Dataeau ='Eau'):
    longueur = removeFLuo(Data)[0]
    intensite = removeFLuo(Data)[1]
    intensiteeau = removeFLuo(Dataeau)[1]
    ratio = []
    for i in range(0,len(intensite)):
        x = intensite[i]/intensiteeau[i]
        ratio.append(x)
    plt.plot(longueur, ratio)
    plt.ylim(0,max(ratio))
    plt.xlim(max(longueur), 0)
    plt.show()
    return longueur, ratio
ratioeau('Heineken')

def pca(Biere, Sucre, Ethanol):
    longueur = ratioeau(Biere)[0]
    intensitebiere = ratioeau(Biere)[1]
    intensiteSucre = ratioeau(Sucre)[1]
    intensiteEthanol = ratioeau(Ethanol)[1]
    df = pd.DataFrame(list(zip(intensitebiere, intensiteSucre, intensiteEthanol, longueur)),
               columns =['Bière', 'Sucre', 'Ethanol', 'Longueur'])

    labels = [intensitebiere, intensiteSucre, intensiteEthanol]

    for i,j in enumerate(labels):
        if i == 0:
            x = 'Bière'
        if i == 1:
            x = 'Sucre'
        if i == 2:
            x = 'Ethanol'
        l = plt.plot(longueur, j, label=x)
        plt.legend(loc="upper left")


    plt.subplots_adjust(hspace=0)
    plt.xlabel('wavelength')
    plt.ylabel('intensity')
    plt.title('Spectra')
    plt.show()

def echantillonage(*alcool):
    intensite = []
    for i,j in enumerate(alcool):
        intensite.append(ratioeau(alcool[i])[1])
        for i in intensite:
            plt.plot(ratioeau(alcool[0])[0], i)
            plt.xlim(max(ratioeau(alcool[0])[0]), 250)
            plt.ylim(0, 20)
    plt.show()
echantillonage('Ethanol70', 'Ethanol65', 'Ethanol20')
