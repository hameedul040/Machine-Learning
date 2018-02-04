# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:46:20 2017

@author: Hameed
"""
import os
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

os.chdir(r'C:\Users\Hameed\Desktop')
td = pd.read_csv('Features.csv')
td['character_class'] = LabelEncoder().fit_transform(td.character)
td.drop('character', axis=1, inplace=True)
td=td.loc[:70000,:]
S=[0.1,0.2,0.4,0.8,1]
trees=[8,16,32,64,128,256]
Scores=[]
for s in S:
    for t in trees:
      etc = ExtraTreesClassifier(n_estimators=t) 
      f = td.sample(frac=s, random_state=0)
      X=f.iloc[:, :-1]
      Y=f.iloc[:, -1]
      acc=cross_validate(etc, X, Y,cv=3)
      print("sample:",s,"  trees:",t,"score:",acc['test_score'].mean())
      Scores.append([s,t,acc['test_score'].mean()])

