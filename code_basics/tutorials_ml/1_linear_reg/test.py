import pandas as pd
import numpy as np
# from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv('homeprices.csv')
print(df)
# define your x-axis
plt.xlabel('area')
# define your y-axis
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='.')
plt.show()