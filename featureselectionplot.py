import pandas as pd
import math

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs

import matplotlib.pyplot as plt

#reading dataset

import pandas as pd
import math

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn.preprocessing import StandardScaler


# Read dataset into a DataFrame
df = pd.read_csv("Master.csv")

#-----moving pawn count prediction to last column-----#
temp_cols=df.columns.tolist()
new_cols=temp_cols[2:] + temp_cols[0:2]
df=df[new_cols]

#-----------------dropping tex fields---------------------#

df = df.drop(['Domain', 'Description', 'DataClasses'], axis=1)

#split into x(input) and y(output variable)

x= df.iloc[:,:-1]
y= df.iloc[:,-1]

#split training and test

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.4, random_state=0)

#building the model

model = LinearRegression()

model_sfs = sfs(model, k_features= "best", forward=True, verbose=2,scoring='r2')
#forward selection
model_sfs= model_sfs.fit(X_train, Y_train)

# feat_names = list(model_sfs.k_feature_names_)

# print( '\n', feat_names)

#plot

plot_sfs(model_sfs.get_metric_dict(), kind= 'std_err')

plt.title("Sequential Forward Selection (w. stanard error)")
plt.ylabel("Performance (R^2)")
plt.grid()
plt.show()


