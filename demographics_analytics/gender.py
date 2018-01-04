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


