# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 01:34:55 2018

@author: Mohammad Doosti Lakhani (nikan.doosti@outlook.com), Hamed Faraji(h.m.d.faraji.h.m.d@gmail.com)
"""

""" In this file we will make some code which will do preprocessing for us on all datasets """
""" the resourses of these datasets are mentioned in README.md file. """


# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = 'datasets/' 
# because we are using local files, you need to download datasets and change the "path" variable
# local folder of your downloaded datasets


def bcw(): 
    # importing dataset
    dataset = pd.read_csv(path+'bcw.csv',
                          names = ['Sample code number','Clump Thickness','Uniformity of Cell Size',
                                   'Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial',
                                   'Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class'])
    dataset= dataset.replace(to_replace='?',value=np.nan)
    #dataset = dataset[dataset.'Bare Nuclei' != np.nan]
    dataset = dataset.dropna(axis =0) # resolving missing values
    dataset = dataset.astype('int64') # casting string valued column to int64
    x = dataset.iloc[:,:-1].values # features
    y = dataset.iloc[:,-1].values # target values
    return (x,y)


def cmc():
    # importing dataset
    dataset = pd.read_csv(path+'cmc.csv', names=["Wife's age","Wife's education","Husband's education",
                                                 "Number of children ever born","Wife's religion",
                                                 "Wife's now working?","Husband's occupation",
                                                 "Standard-of-living index","Media exposure","Contraceptive method used"])
    x = dataset.iloc[:,:-1].values # features
    y = dataset.iloc[:,-1].values # target values
    return (x,y)


def glass():
    # importing dataset
    dataset = pd.read_csv(path+'glass.csv', names= ['Id','refractive index','Magnesium','Aluminum','Silicon','Potassium','Calcium','Barium','Iron','glass'])
    x = dataset.iloc[:,:-1].values # features
    y = dataset.iloc[:,-1].values # target values
    return (x,y)


def iris():
    # importing dataset
    dataset = pd.read_csv(path+'iris.csv', names= ['sepal length','sepal width','petal length','petal width','class'])
    x = dataset.iloc[:,:-1].values # features
    y = dataset.iloc[:,-1].values # target values
    
    # encoding categorial data types to labelEncoder
    from sklearn.preprocessing import LabelEncoder
    labelencoder_y = LabelEncoder()
    labelencoder_y = labelencoder_y.fit(y)
    y = labelencoder_y.transform(y)  # 0 for 'Iris-setosa', 1 for 'Iris-versicolor', 2 for 'Iris-virginica'
    return (x,y)


def vowel():
    # importing dataset
    dataset = pd.read_csv(path+'vowel.csv', names= ['vowel','type 1 frq','type 2 frq','type 3 frq'])
    x = dataset.iloc[:,1:].values # features
    y = dataset.iloc[:,0].values # target values
    return (x,y)

def wine():
    # importing dataset
    dataset = pd.read_csv(path+'wine.csv', names= ['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315','Proline'])
    x = dataset.iloc[:,1:].values # features
    y = dataset.iloc[:,0].values # target values
    return (x,y)

tempx,tempy = bcw()

print(tempx[8])