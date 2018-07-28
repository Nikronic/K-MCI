# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 01:11:10 2018

@author: Mohammad Doosti Lakhani (nikan.doosti@outlook.com), Hamed Faraji(h.m.d.faraji.h.m.d@gmail.com)
"""
"""
This is the implementatino of Candidate class. Candidate class is the most important class because it has
the structure of answer based on cluster centers and other important parameters to control explotation and exploration. 
"""


# importing libraries
import random
    

class Candidate:    
    def __init__(self,clusters,sampling_interval, variation_count,fitness=-1):
        self.clusters = clusters
        self.sampling_interval = sampling_interval 
        self.variation_count = variation_count
        self.random_number
        self.fitness = fitness
        self.centers = None
        
    def random_number(self):
        self.random_number = random.random()
        
    #def describe(self):
        #print("Candidate with features={}, fitness={}".format(self.clusters.describe(),self.fitness))