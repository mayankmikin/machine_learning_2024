import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
print("Setup complete.")
# print(reviews)
indexes_to_find=[reviews.columns.get_loc('country'),reviews.columns.get_loc('variety')]
print(indexes_to_find)
df =reviews.iloc[0:100,indexes_to_find]
print(df)