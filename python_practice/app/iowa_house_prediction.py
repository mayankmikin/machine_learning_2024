# Code you have previously used to load data
import pandas as pd
import numpy as np

# # Path of the file to read
# iowa_file_path = 'train.csv'

# home_data = pd.read_csv(iowa_file_path)
# # print(home_data)
# y = home_data['SalePrice']
# # Create the list of features below
# feature_names = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]

# # Select data corresponding to features in feature_names
# X = home_data[feature_names]
# # Review data
# # print description or statistics from X
# # print(X.describe())

# # print the top few lines
# # print(X.head(5))

# ########### DEFINE what type of mahcine learning model it is
# from sklearn.tree import DecisionTreeRegressor
# #specify the model. 
# #For model reproducibility, set a numeric value for random_state when specifying the model
# iowa_model = DecisionTreeRegressor(random_state=1)

# # Fit the model
# iowa_model.fit(X,y)

# ## Make Predictions
# predictions = iowa_model.predict(X)
# print(predictions)


# ##### evaluate

# # Step 1: Split Your Data
# # Use the train_test_split function to split up your data.
# # Give it the argument random_state=1 so the check functions know what to expect when verifying your code.
# # Recall, your features are loaded in the DataFrame X and your target is loaded in y.

# # Import the train_test_split function and uncomment
# from sklearn.metrics import mean_absolute_error
# from sklearn.model_selection import train_test_split

# # fill in and uncomment
# train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# # Specify the model
# iowa_model = DecisionTreeRegressor(random_state=1)

# # Fit iowa_model with the training data.
# iowa_model.fit(train_X, train_y)

# # Predict with all validation observations
# val_predictions = iowa_model.predict(val_X)
# from sklearn.metrics import mean_absolute_error
# val_mae = mean_absolute_error(val_y, val_predictions)

# # uncomment following line to see the validation_mae
# print(val_mae)




########### with validation and over fitting and underfitting 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


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
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
#EVALUATE
val_mae = mean_absolute_error(val_predictions, val_y)
# print("Validation MAE: {:,.0f}".format(val_mae))

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# mae_list=[]
# for i in candidate_max_leaf_nodes:
#     mae_list.append(get_mae(i,train_X, val_X, train_y, val_y))
  
#print(min(mae_list))
#print(mae_list.index(min(mae_list)))  
# print(candidate_max_leaf_nodes[mae_list.index(min(mae_list))])  

candidate_mae= list(map(lambda x: get_mae(x,train_X, val_X, train_y, val_y),candidate_max_leaf_nodes))

# # Convert the list to a numpy array
candidate_mae = np.array(candidate_mae)
# # Find the minimum value and its index
min_value = np.min(candidate_mae)
min_index = np.argmin(candidate_mae)

print("The minimum value is:", min_value)
print("The position (index) of the minimum value is:", min_index)
print("So optimal leaf node will be :", candidate_max_leaf_nodes[min_index])
