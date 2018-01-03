import pandas as pd
import matplotlib.pyplot as plt

## 性别
data1 = pd.read_csv('../data/big-data-1_enrolments.csv',usecols=[6])
grouped1 = data1.groupby('gender')
#print(grouped1.describe())
Unknown = data1[(data1.gender == 'Unknown')].count()
female = data1[data1.gender == 'female'].count()
male = data1[(data1.gender == 'male')].count()
nonbinary = data1[(data1.gender == 'nonbinary')].count()
other = data1[data1.gender == 'other'].count()

#s=pd.DataFrame([Unknown,female,male,nonbinary,other],index=['Unknown','female','male','nonbinary','other'])
s=pd.DataFrame([female,male,nonbinary,other],index=['female','male','nonbinary','other'])
s.plot(kind='bar')
plt.xlabel('gender')
plt.ylabel('')
plt.show()






data2 = pd.read_csv('../data/big-data-1_step-activity.csv')

#data3 = pd.DataFrame(data,data2)
#grouped = data3.groupby("learner_id")
#print(grouped.describe())

outfile = pd.merge(data1,data2, how='left',left_on='learner_id',right_on='learner_id')
outfile.to_csv('data/outfile.csv',index=False, encoding='gbk')
data3 = pd.read_csv('data/outfile.csv')
grouped = data3.groupby("learner_id")
#print(grouped.describe())

