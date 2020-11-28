#import libraries
import sys
#!conda install --yes --prefix {sys.prefix} -c districtdatalabs yellowbrick
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graph_display(X, y, labelX = None, labely = None, title = None, pred = None, c1X = None, c1y = None):
    plt.scatter(X, y, c=pred, s = 25) 
    plt.scatter(c1X, c1y, c='black', s=100);
    plt.xlabel(labelX)
    plt.ylabel(labely)
    
def kmeans_groups(min, max, df, metric = 'calinski_harabasz'):
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(min,max), metric = metric, timings=False)
    visualizer.fit(df)
    visualizer.show()
    
def kmeans_clust (n_clusters, df):
    k_means = KMeans(n_clusters= n_clusters)
    k_means.fit(df)
    y_hat = k_means.predict(df)
    return k_means, y_hat