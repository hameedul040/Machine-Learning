# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:27:52 2017

@author: Hameed
"""


import os
import numpy as np
import pandas as pd
from scipy.misc import imread
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.tree import ExtraTreeClassifier, DecisionTreeClassifier
from sklearn.neighbors import NearestCentroid, KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import cross_validate, GridSearchCV, learning_curve
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.calibration import calibration_curve
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
#os.chdir(r'C:\Users\Hameed\Desktop')
##cl = pd.read_csv('Features.csv')
#cl['character_class'] = LabelEncoder().fit_transform(cl.character)
#cl.drop('character', axis=1, inplace=True)
#cl=cl.loc[:70000,:]
#cl.apply(pd.to_numeric)
#total_rows=len(cl.axes[0])
#total_cols=len(cl.axes[1])
#
#
#df_mix = cl.sample(frac=1, random_state=0)
#
#
#
##applyng naive bayes classifier
#
#Xtrain=df_mix.iloc[0:49000, :-1]
#Ytrain=df_mix.iloc[0:49000,-1]
#
#Xtest=df_mix.iloc[49000:70000, :-1]
#Ytest=df_mix.iloc[49000:70000, -1]
#clf = GaussianNB()
#clf.fit(Xtrain, Ytrain)
#
#GNscore=clf.score(Xtest,Ytest)

lr = LogisticRegression()
gnb = GaussianNB()
svc = LinearSVC(C=1.0)
rfc = RandomForestClassifier()
rdg=RidgeClassifier()
brn= BernoulliNB()
ext=ExtraTreeClassifier()
dtc=DecisionTreeClassifier()
nc=NearestCentroid()
knn=KNeighborsClassifier()


classifiers=[lr,gnb,svc,rfc,rdg,brn,ext,dtc,nc,knn]

test_scores = []
train_scores = []
fit_time = []
score_time = []
scoretable=[]
for clf in classifiers:
    scores = cross_validate(clf, df_mix.iloc[:, :-1], df_mix.iloc[:, -1])
	scoretable.append(scores)

