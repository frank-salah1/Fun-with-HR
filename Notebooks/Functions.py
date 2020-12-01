#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import cross_validate
from sklearn import metrics
import seaborn as sns 
from sklearn.preprocessing import StandardScaler

def log_reg(X, y,cv=5):
    logreg = LogisticRegression(penalty = 'none')
    crossval = cross_validate(logreg, X,y, return_train_score=True, scoring='accuracy', return_estimator=True, cv = cv)
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