import pandas as pd
from skleran.metrics import fbeta_score
from sklearn.metrics import accuracy_score

#import .csv into pandas dataframe
data_x = pd.read_csv("./training_data/x_train.csv")
data_y = pd.read_csv("./training_data/y_train.csv")

#print(data_x)
#print(data_y)

#merge dataframes base on GeneId column
data = pd.merge(data_x, data_y, left_on='GeneId', right_on='GeneId')
print(data)
