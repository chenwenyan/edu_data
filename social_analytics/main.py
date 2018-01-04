import pandas as pd
import matplotlib.pyplot as mpl
import glob

data1 = pd.read_csv('../data/big-data-1_enrolments.csv',usecols=[0])
data2 = pd.read_csv('../data/big-data-1_step-activity.csv')
#Joiners
joiners = data1[data1.learner_id != ''].count()
print(joiners)

#learners
grouped = data2.groupby('learner_id')
learners = grouped.size()
print(learners)

#Active Learners
ActiveLearners = data2[data2['last_completed_at'].notnull()].groupby('learner_id').size()
print(ActiveLearners)

#Returning Learners
ReturningLearners = data2[(data2['last_completed_at'].notnull()) & (data2['week_number'] != 1)].groupby('learner_id').size()
print(ReturningLearners)

#Fully Participating Learners
FullyParticipatingLearners = data2[data2['last_completed_at'].notnull()].groupby('week_number','step_number').size()















