import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font',size=20)
sns.set(style="white")
sns.set(style="whitegrid",color_codes=True)

col_names = ['age','workclass','fnlwgt','education','education_num',
             'marital','occupation','relationship','race','sex','capital_gain',
             'capital_loss','hours_per_week','native_country','y']

datatypes = {'age':np.int32,'fnlwgt':np.int32,'education_num':np.int32,'capital_gain':np.int32,
             'capital_loss':np.int32,'hours_per_week':np.int32,'y':np.str}

data = pd.read_csv("adult_data.csv",header=0,names=col_names,dtype=datatypes)

print(data.head())

print(data.columns)

print(data.shape)

#mapping = {"<=50K":0,">50K":1}

data['new_y'] = np.where(data['y'] == " <=50K", '0','1')
print(data['new_y'].value_counts())
print(data['new_y'])
print(data.head())


data = data.drop('y',axis=1)
print(data.head())

data = data.replace(" ?",np.NaN)
data = data.dropna()
print(data.shape)

data['sex'].value_counts()
data['marital' == '']

sns.countplot(x='new_y',data=data,palette='hls')
data.age.hist()

plt.figure(figsize=(12,6))
sns.countplot(x='workclass',data=data,hue='new_y')

plt.figure(figsize=(12,6))
sns.countplot(x='education',data=data,hue='new_y')

plt.figure(figsize=(12,6))
sns.countplot(x='marital',data=data,hue='new_y')
plt.figure(figsize=(12,6))
sns.countplot(x='occupation',data=data,hue='new_y')

df = data[(data['new_y'] == '1')]




data.groupby('marital').mean()

data.drop(['fnlwgt','education'],axis=1)
plt.figure(figsize=(12,10))
sns.countplot(x='new_y',data=data,hue='race',palette='hls')

