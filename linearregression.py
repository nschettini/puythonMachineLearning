import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df = pd.read_csv('/Users/nschettini/Documents/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/USA_Housing.csv')

df.columns

sns.pairplot(df)

sns.distplot(df['Price'])

sns.heatmap(df.corr())
