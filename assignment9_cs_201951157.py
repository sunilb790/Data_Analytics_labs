# -*- coding: utf-8 -*-
"""Assignment9_CS_201951157.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pkw9u5Wrsvumx5H9TGe3gnHMbAVChjW0

#CS312 DATA ANALYTICS AND VISUALIZATION  
#SUNIL BHENSPALIYA
#201951157 (CSE)
#LAB ASSIGNMENT :- 9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('/content/sample_data/weight-height.csv')['Height']
data.head()

_ = plt.hist(data, bins=200)
standard_error = np.std(data)/(np.sqrt(len(data)))
standard_error

sample_data = np.random.choice(data,100,replace=False)
_ = plt.hist(sample_data,bins=10)
standard_error = np.std(sample_data)/np.sqrt(len(sample_data))
standard_error

number_of_samples=10000
size_of_sample=100
sample_mean=[]
for i in range(number_of_samples):
    sample_mean.append(np.mean(np.random.choice(data,size_of_sample,replace=False)))

_=plt.hist(sample_mean,bins=100)
standard_error=np.std(sample_mean)/np.sqrt(len(sample_mean))
standard_error

number_of_samples=10000 # R times
size_of_sample=300  # n
sample_mean=[]
for i in range(number_of_samples):
    # Calulate mean for n samples
    sample_mean.append(np.mean(np.random.choice(data,size_of_sample,replace=True)))

_=plt.hist(sample_mean,bins=100)
standard_error=np.std(sample_mean)/np.sqrt(len(sample_mean))
standard_error

CI=0.95
sorted_means=np.sort(sample_mean)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower level :", sorted_means[idx])
print("Upper level :", sorted_means[l-idx-1])

CI=0.9
sorted_means=np.sort(sample_mean)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower level :", sorted_means[idx])
print("Upper level :", sorted_means[l-idx-1])

CI=0.8
sorted_means=np.sort(sample_mean)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower level :", sorted_means[idx])
print("Upper level :", sorted_means[l-idx-1])