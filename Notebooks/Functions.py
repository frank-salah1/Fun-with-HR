#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import cross_validate
from sklearn import metrics
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans

def log_reg(X, y,cv=5):
    logreg = LogisticRegression(penalty = 'none')
    crossval = cross_validate(logreg, X,y, return_train_score=True, scoring='accuracy', return_estimator=True, cv = cv)
    return crossval

def lin_reg(X, y, cv=5):
    lrreg = LinearRegression()
    crossval = cross_validate(lrreg, X,y, return_train_score=True, scoring='r2', return_estimator=True, cv=cv)
    return crossval

def accuracy_display(estimator, X, y, label = '' ):
    predictions = estimator.predict(X)
    score = estimator.score(X, y)
    cm = metrics.confusion_matrix(y, predictions)
    plt.figure(figsize=(9,9))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Pastel1');
    if label != '':
        label = ': ' + label
    plt.ylabel('Actual label' + label);
    plt.xlabel('Predicted label' + label);
    title = 'Accuracy Score: {0}'.format(score)
    plt.title( title, size = 15);
    plt.show()

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
