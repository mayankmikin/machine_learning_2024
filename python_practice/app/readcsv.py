import pandas as pd

df = pd.read_csv('data.csv')

# print(df.to_string()) 
df1=df[['Duration','Pulse']]
print(df1)
