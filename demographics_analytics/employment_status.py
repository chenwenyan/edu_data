import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## 年龄范围
# data = pd.read_csv('../data/Run 1/big-data-1_enrolments.csv',usecols=[10])
# data = pd.read_csv('../data/Run 2/big-data-2_enrolments.csv',usecols=[10])
# data = pd.read_csv('../data/Run 3/big-data-3_enrolments.csv',usecols=[10])
# data = pd.read_csv('../data/Run 5/the-mind-is-flat-5_enrolments.csv',usecols=[10])
# data = pd.read_csv('../data/Run 6/the-mind-is-flat-6_enrolments.csv',usecols=[10])
# data = pd.read_csv('../data/Run 7/the-mind-is-flat-7_enrolments.csv',usecols=[10])
data = pd.read_csv('../data/combination/big-data-1_enrolments.csv',usecols=[10])
grouped = data.groupby('employment_status')
#print(grouped.describe())

Unknown = data[data.employment_status == 'Unknown'].count()
full_time_student = data[data.employment_status == 'full_time_student'].count()
looking_for_work = data[data.employment_status == 'looking_for_work'].count()
not_working = data[data.employment_status == 'not_working'].count()
retired = data[data.employment_status == 'retired'].count()
self_employed = data[data.employment_status == 'self_employed'].count()
unemployed = data[data.employment_status == 'unemployed'].count()
working_full_time = data[data.employment_status == 'working_full_time'].count()
working_part_time = data[data.employment_status == 'working_part_time'].count()

s = pd.DataFrame([full_time_student,looking_for_work,not_working,retired,self_employed,unemployed,working_full_time,
                  working_part_time],index=['full_time_student','looking_for_work','not_working','retired',
                                            'self_employed','unemployed','working_full_time','working_part_time'])

s.plot(kind='bar')
plt.xticks(np.arange(8),('full_time_student','looking_for_work','not_working','retired','self_employed','unemployed','working_full_time','working_part_time'),rotation=27)
plt.xlabel('employment_status')
plt.ylabel('')
plt.show()
