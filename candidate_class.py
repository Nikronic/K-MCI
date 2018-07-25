# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 01:11:10 2018

@author: Mohammad Doosti Lakhani
"""
class Candidate:

    def __init__(self,features,psi, t, r,fitness=-1):
        self.features = features
        self.psi = psi
        self.t = t
        self.r = r
        self.fitness = fitness

        
    def show_info(self):
        print("Candidate with features={}, fitness={}".format(self.features,self.fitness))
        
    def random_generator(self):
        


""" numberOfVariations = t
    iterationCount = n
    convergencePar = ep
    samplingIntervalReduction = r
    samplingInterval = psi
    candidatesCount   
"""

