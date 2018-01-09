import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## 年龄范围
# data = pd.read_csv('../data/Run 1/big-data-1_enrolments.csv',usecols=[8])
# data = pd.read_csv('../data/Run 2/big-data-2_enrolments.csv',usecols=[8])
# data = pd.read_csv('../data/Run 3/big-data-3_enrolments.csv',usecols=[8])
# data = pd.read_csv('../data/Run 5/the-mind-is-flat-5_enrolments.csv',usecols=[8])
# data = pd.read_csv('../data/Run 6/the-mind-is-flat-6_enrolments.csv',usecols=[8])
# data = pd.read_csv('../data/Run 7/the-mind-is-flat-7_enrolments.csv',usecols=[8])
data = pd.read_csv('../data/combination/big-data-1_enrolments.csv',usecols=[8])
grouped = data.groupby('age_range')
#print(grouped.describe())
#Unknown = data[(data.age_range == 'Unknown')].count()
under18 = data[data.age_range == '<18'].count()
_18_25 = data[(data.age_range == '18-25')].count()
_26_35 = data[(data.age_range == '26-35')].count()
_36_45 = data[(data.age_range == '36-45')].count()
_46_55 = data[(data.age_range == '46-55')].count()
_56_65 = data[(data.age_range == '56-65')].count()
up65 = data[data.age_range == '>65'].count()

#s=pd.DataFrame([Unknown,under18,_18_25,_26_35,_36_45,_46_55,_56_65,up65],index=['Unknown','<18','18-25','26-35','36-45',
s=pd.DataFrame([under18,_18_25,_26_35,_36_45,_46_55,_56_65,up65],index=['<18','18-25','26-35','36-45','46-55','55-65',
                                                                        '>65'])
s.plot(kind='bar')
plt.xticks(np.arange(7),('<18','18-25','26-35','36-45','46-55','55-65','>65'),rotation=17)
plt.xlabel('age_range')
plt.ylabel('')
plt.show()