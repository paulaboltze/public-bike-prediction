import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
import pickle

## read the file

df=pd.read_csv('final_df.csv')


## preprocess

df = df[['hour','temp', 'rhum','total']]


#df.is_holiday = df.is_holiday.astype('category')
#df.weekday = df.weekday.astype('category')

#df = pd.get_dummies(df)

## modelling

X = df.drop(columns = ['total'])
y = df['total']



rf = RandomForestRegressor(max_depth=11, random_state=42)
rf.fit(X,y)
pickle.dump(rf, open('model.pkl','wb'))

