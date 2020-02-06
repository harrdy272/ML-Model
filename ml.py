import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('dataset.csv')
X = data.iloc[:,::-1].values
y= data.iloc[:,10].values
