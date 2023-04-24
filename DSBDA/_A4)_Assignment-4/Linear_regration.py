# %%
import pandas as pd

import numpy as np 

import matplotlib.pyplot as plt  

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

url="http://bit.ly/w-data"
data=pd.read_csv(url)

data.plot(x='Hours',y='Scores',style='*')
plt.title('Houres vs Scores')
plt.xlabel('Houres')
plt.ylabel('Scores')
plt.show()

x= data.iloc[:, :-1].values
y= data.iloc[:, 1].values

x_train,x_test ,y_train ,y_test =train_test_split(x,y, test_size=0.2,random_state=0)

regressor=LinearRegression()
regressor.fit(x_train,y_train)
print("trining completed")

line=regressor.coef_ *x +regressor.intercept_
plt.scatter(x,y)
plt.plot(x,line)
plt.show()

print(x_test)
y_pre = regressor.predict(x_test)
df=pd.DataFrame({'Actual':y_test,'Predicted':y_pre})
print(df)

#test with own data
hours=10.25

own_precent=regressor.predict([[hours]])
print("No of hours={}".format(hours))
print("predicted percentage={}".format(own_precent[0]))

#Evaluating the model
print("Mean absolute error:",mean_absolute_error(y_test,y_pre))

# %%