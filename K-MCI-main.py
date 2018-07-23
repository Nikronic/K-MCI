# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:46:04 2018

@author: HaMeD
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from datasets import bcw,wine

wcss = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    tempx,tempy = wine()
    kmeans.fit(tempx)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 10), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(tempx)

# Visualising the clusters
plt.scatter(tempx[y_kmeans == 0, 0], tempx[y_kmeans == 0, 1], s = 10, c = 'red', label = 'Cluster 1')
plt.scatter(tempx[y_kmeans == 1, 0], tempx[y_kmeans == 1, 1], s = 10, c = 'blue', label = 'Cluster 2')
plt.scatter(tempx[y_kmeans == 2, 0], tempx[y_kmeans == 2, 1], s = 10, c = 'green', label = 'Cluster 3')
plt.scatter(tempx[y_kmeans == 3, 0], tempx[y_kmeans == 3, 1], s = 10, c = 'cyan', label = 'Cluster 4')
plt.scatter(tempx[y_kmeans == 4, 0], tempx[y_kmeans == 4, 1], s = 10, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
'''print(tempx)
print(kmeans.cluster_centers_[:, 0])'''
print(len(tempx))