# -*- coding: utf-8 -*-
"""Assignment5_CS_201951157.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-IXLUtfIm5sPtPng1PwxMUgxqDjl3Ivm

**SUNIL BHENSPALIYA**
**201951157**
*ASSIGNMENT 5*
"""

!pip install joypy
!pip install squarify
!pip install plotly

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from statsmodels.graphics.mosaicplot import mosaic
from joypy import joyplot #!pip install joypy
import squarify # pip install squarify
import plotly.express as px # pip install plotly

data = pd.read_csv("/content/sample_data/heart.csv")
data.head()

updated_data = data[data["thal"] >= 3]

sns.scatterplot(
    data = updated_data, x="cp", y="age",
    sizes = (20, 200), legend="full"
)

fig = sns.PairGrid(updated_data[["age", "sex", "cp", "trestbps", "slope"]])
fig.map(sns.scatterplot)

import plotly.express as px

fig = px.parallel_categories(data, dimensions=['sex', 'cp',   'fbs',   'slope', 'ca', 'thal','target'], color="age", color_continuous_scale=px.colors.sequential.Plasma)
fig.show()