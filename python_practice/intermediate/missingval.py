import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv('train.csv', index_col='Id')
X_test_full = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, we'll use only numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)

null_columns=X_train.isnull().sum()
# print(null_columns)
# print(null_columns[null_columns >0])
# print(len(null_columns[null_columns >0]))

# Getting the shape of the DataFrame
# shape = X_train.shape
# row_count = shape[0]
# column_count = shape[1]
# print(row_count,column_count)
# print(sum(null_columns[null_columns >0]))
cols_with_missing_vals=null_columns[null_columns >0]
# print(cols_with_missing_vals.index.tolist())

reduced_X_train = X_train.dropna(axis=1)
reduced_X_valid = X_valid.dropna(axis=1)
print(reduced_X_train.shape)
print(reduced_X_valid.shape)