# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 01:11:10 2018

@author: Mohammad Doosti Lakhani
"""
"""
This is the implementatino of Candidate class. Candidate class is the most important class because it has
the structure of answer based on cluster centers and other important parameters to control explotation and exploration. 
"""


# importing libraries
import random


class Candidate:
    def __init__(self,clusters,centers,sampling_interval, variation_count, random_number,fitness=-1):
        self.clusters = clusters
        self.sampling_interval = sampling_interval 
        self.variation_count = variation_count 
        self.random_number = random_number
        self.fitness = fitness
        self.centers = centers
        
    def random_number(self):
        self.random_number = random.random()
        
    #def describe(self):
        #print("Candidate with features={}, fitness={}".format(self.clusters.describe(),self.fitness))
    
    