########### with validation and over fitting and underfitting 
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Path of the file to read
iowa_file_path = 'train.csv'
#READ DATA 
home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalePrice
# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]
# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model DEFINE
rf_model = RandomForestRegressor(random_state=1)
# Fit Model
rf_model.fit(train_X,train_y)
# predict the values
melb_preds =rf_model.predict(val_X)
# Calculate the mean absolute error of your Random Forest model on the validation data
mae = mean_absolute_error(val_y,melb_preds)
print(mae)


