# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 01:27:52 2017

@author: Hameed
"""



import numpy as np
import pandas as pd
from scipy.misc import imread


import os
WorkFolder= os.getcwd()
ParentFolder = os.path.join(WorkFolder, 'Restructure')

pixels = np.array(['pixel_{:04d}'.format(x) for x in range(1024)])
flag = True

for char_name in sorted(os.listdir(ParentFolder)):
    char_dir = os.path.join(ParentFolder, char_name)
    img_df = pd.DataFrame(columns=pixels)
    
    for img_file in sorted(os.listdir(char_dir)):
        image = pd.Series(imread(os.path.join(char_dir, img_file)).flatten(), index=pixels)
        img_df = img_df.append(image.T, ignore_index=True)
        
    img_df = img_df.astype(np.uint8)
    img_df['character'] = char_name
    
    img_df.to_csv('data.csv', index=False, mode='a', header=flag)
    flag=False
    
    print('=', end='')
    
    
