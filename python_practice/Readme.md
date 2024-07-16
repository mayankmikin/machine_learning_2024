### create e new virtual environment
> python -m venv aqua

#####
Here, aqua is the name of the directory where the virtual environment will be created. You can choose any name you like.

#### CMDS 
> source aqua/bin/activate
> deactivate

#### PIP - libraries install and setup 
###### SAVE in requirement .txt
> pip freeze > requirements.txt
##### install packages befofe deployment/local environment command 
> pip install -r requirements.txt






### Building Your Model
You will use the scikit-learn library to create your models. When coding, this library is written as sklearn, as you will see in the sample code. Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

The steps to building and using a model are:
#### DFPE
## Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
## Fit: Capture patterns from provided data. This is the heart of modeling.
## Predict: Just what it sounds like
## Evaluate: Determine how accurate the model's predictions are.




## Overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions, or
## Underfitting: failing to capture relevant patterns, again leading to less accurate predictions.