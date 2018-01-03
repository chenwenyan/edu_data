from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from pandas import DataFrame as df

column=load_iris().feature_names
data=load_iris().data
target=load_iris().target
df1=df(data,columns=column)
df2=df(target,columns=['target'])
data_df=pd.concat([df1,df2],axis=1)
print(data_df.shape)
data_df.describe()