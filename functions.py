# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:51:08 2018

@author: Mohammad Doosti Lakhani (nikan.doosti@outlook.com), Hamed Faraji(h.m.d.faraji.h.m.d@gmail.com)
"""


""" importing neccassry libraries """
import numpy as np
from sklearn.cluster import KMeans
import random
import datasets
 

def roulette_wheel_selection(inertia_array):
    maximum = np.sum(inertia_array)
    pick = random.uniform(0, maximum)
    current = 0
    for fitness in inertia_array:
        current += fitness
        if current > pick:
            return fitness

def probability(inertia_array,i):
    return (1/inertia_array[i])/(1/(np.sum(inertia_array)))

# we get inertia_ with kmean and among all inertia_ of all candidate we choose minimum as best 
def best_fitness(array_of_inertia):
    return np.amin(array_of_inertia)

def sampling_interval(input_array):
    Maxes = np.amax(input_array,axis=0)
    Mins  = np.amin(input_array,axis=0)
    return (Maxes,Mins)

def mutation(candidate_array):
    Y = random.random()
    New_candidate = Mutant_candidate = Trial_candidate = candidate_array 
    for x in range(len(candidate_array)):
        a = np.full(len(candidate_array), 1/(len(candidate_array)-1))
        a[x] = 0
        temp = np.random.choice(len(candidate_array), 3, replace = False, p=a)
        for i in range(len(candidate_array[0].features)):
            Mutant_candidate[x].features[i][0] = candidate_array[temp[0]].features[i][0]+ random.random()*(candidate_array[temp[1]].features[i][0] - candidate_array[temp[2]].features[i][0])
            if random.random() < Y:
                Trial_candidate[x].features[i][0] = Mutant_candidate[x].features[i][0] #Trial & Mutant must be copy of same candidate
        if fitness(candidate_array[x]) > fitness(Trial_candidate[x]):
            New_candidate[x] = Trial_candidate[x]
    return New_candidate

def fitness(sample):
    return True

a = [[5,3],[3.5,5],[5.25,5.1],[6,3],[1.5,0],[2.76,8]]
mutation(a)

# Fitting K-Means to a dataset
def doKmeans(x,clusters_count):
    kmeans = KMeans(n_clusters = clusters_count, init = 'k-means++', random_state = 0)
    y_predict_kmeans = kmeans.fit_predict(x)
    return (y_predict_kmeans,kmeans.cluster_centers_,kmeans.inertia_)