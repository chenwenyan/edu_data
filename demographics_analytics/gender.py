import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## 性别
# data = pd.read_csv('../data/Run 1/big-data-1_enrolments.csv',usecols=[6])
# data = pd.read_csv('../data/Run 2/big-data-2_enrolments.csv',usecols=[6])
# data = pd.read_csv('../data/Run 3/big-data-3_enrolments.csv',usecols=[6])
# data = pd.read_csv('../data/Run 5/the-mind-is-flat-5_enrolments.csv',usecols=[6])
# data = pd.read_csv('../data/Run 6/the-mind-is-flat-6_enrolments.csv',usecols=[6])
# data = pd.read_csv('../data/Run 7/the-mind-is-flat-7_enrolments.csv',usecols=[6])
data = pd.read_csv('../data/combination/big-data-1_enrolments.csv',usecols=[6])
grouped1 = data.groupby('gender')
#print(grouped1.describe())
Unknown = data[(data.gender == 'Unknown')].count()
female = data[data.gender == 'female'].count()
male = data[(data.gender == 'male')].count()
nonbinary = data[(data.gender == 'nonbinary')].count()
other = data[data.gender == 'other'].count()

#s=pd.DataFrame([Unknown,female,male,nonbinary,other],index=['Unknown','female','male','nonbinary','other'])
s=pd.DataFrame([female,male,nonbinary,other],index=['female','male','nonbinary','other'])
s.plot(kind='bar', stacked=True)
plt.xticks(np.arange(4),('female','male','nonbinary','other'),rotation=27)
plt.xlabel('gender')
plt.ylabel('')
plt.show()

# val_ls = np.array([female,male,nonbinary,other])
# scale_ls = Runge(4)
# index_ls = ['female','male','nonbinary','other']
# idx = np.aRunge(len(index_ls))
# plt.bar(idx,val_ls)
# plt.xticks(idx,index_ls)
# plt.xlabel('gender')
# plt.ylabel('')
# plt.title('xxx')






data2 = pd.read_csv('../data/big-data-1_step-activity.csv')

#data3 = pd.DataFrame(data,data2)
#grouped = data3.groupby("learner_id")
#print(grouped.describe())

# outfile = pd.merge(data,data2, how='left',left_on='learner_id',right_on='learner_id')
# outfile.to_csv('data/outfile.csv',index=False, encoding='gbk')
# data3 = pd.read_csv('data/outfile.csv')
# grouped = data3.groupby("learner_id")
#print(grouped.describe())

