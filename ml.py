import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('dataset.csv')
X = data.iloc[:,::-1].values
y= data.iloc[:,10].values

from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X,y,test_size=0.2,random_state=0)
