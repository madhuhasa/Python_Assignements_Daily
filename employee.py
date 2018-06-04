import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

#from sklearn import LinearRegression

emp_data = pd.read_csv("employee_data.csv")
print(emp_data.columns)
print(emp_data.head())
print(emp_data.describe())

print(emp_data.corr())

sns.countplot(x='Department',data=emp_data)
sns.pairplot(emp_data,hue='Department')

emp_data['Department'] = emp_data['Department'].astype('category').cat.codes
print(emp_data.head())

lr = linear_model.LinearRegression()
y = emp_data['Salary']
X = emp_data[['Department', 'Worked_Hours', 'Certification', 'Experience_in_years']]
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.33)
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)

print(y_test)
print(y_pred)





