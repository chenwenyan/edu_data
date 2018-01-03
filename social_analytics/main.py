import pandas as pd
import matplotlib.pyplot as mpl

data1 = pd.read_csv('../data/big-data-1_enrolments.csv',usecols=[0])
data2 = pd.read_csv('../data/big-data-1_step-activity.csv')

outfile = pd.merge(data1,data2, how='left',left_on='learner_id',right_on='learner_id')
outfile.to_csv('../data/outfile.csv',index=False, encoding='gbk')
data3 = pd.read_csv('../data/outfile.csv')
grouped = data3.groupby("learner_id")
print(grouped.describe())

dataform = grouped.describe()

#Joiners
a = data3(dataform.count == 0.0).count()
print('erweyrweyrweuwerwer')
print(a)
