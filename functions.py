# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:51:08 2018

@author: Mohammad Doosti Lakhani (nikan.doosti@outlook.com), Hamed Faraji(h.m.d.faraji.h.m.d@gmail.com)
"""


""" importing neccassry libraries """
import numpy as np
from sklearn.cluster import KMeans
from datasets import wine
 

class Candidate:
    idn = 0

    def __init__(self,idn,features,psi, t, r,fitness=-1):
        self.features = features
        self.psi = psi
        self.t = t
        self.r = r
        self.idn = idn # a simple id for counting and tracing.
        idn = idn+1
        self.fitness = fitness

        
    def show_info(self):
        print("Candidate with ID={}, features={}, fitness={}".format(self.idn,self.features,self.fitness))


""" numberOfVariations = t
    iterationCount = n
    convergencePar = ep
    samplingIntervalReduction = r
    samplingInterval = psi
    candidatesCount   
"""


def initialize(c, psi, r, ep, n, t):
    all_candidates = np.empty(c,dtype='object')    
    return 0


""" we calculate the probability of each candidate based on its fitness.
    all_candidates = array of all candidates 
    candidate = the candidate which we want its probability"""
def probability(candidate,all_candidates):
    return (1/candidate.fitness)/(1/(np.sum([x.fitness for x in all_candidates])))

def fitness():
    return

def interval(input_array) :
    Maxes = np.max(input_array,axis=0)
    Mins  = np.min(input_array,axis=0)
    return (Maxes,Mins)

def mutation(candidate_array):
    for x in range(len(candidate_array)):
        a = np.full(len(candidate_array), 1/(len(candidate_array)-1))
        a[x] = 0
        temp = np.random.choice(len(candidate_array), 3, replace = False, p=a)
        for i in range(len(candidate_array[0].features)):
        Mutant_candidate[x].features[i][0] = candidate_array[temp[0]].features[i][0]+ random.random()*(candidate_array[temp[1]].features[i][0] - candidate_array[temp[2]].features[i][0])




a = [[5,3],[3.5,5],[5.25,5.1],[6,3],[1.5,0],[2.76,8]]
mutation(a)
# Fitting K-Means to a dataset
def doKmeans(x,clusters_count):
    kmeans = KMeans(n_clusters = clusters_count, init = 'k-means++', random_state = 42)
    y_predict_kmeans = kmeans.fit_predict(x)
    return y_predict_kmeans