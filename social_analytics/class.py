# coding=gbk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import convert

# data2 = pd.read_csv('../data/Run 1/big-data-1_comments.csv', usecols=[0, 1, 2, 5, 9],skip_blank_lines=True )
# data2 = pd.read_csv('../data/Run 2/big-data-2_comments.csv', usecols=[0, 1, 2, 5, 9],skip_blank_lines=True )
# data2 = pd.read_csv('../data/Run 3/big-data-3_comments.csv', usecols=[0, 1, 2, 5, 8],skip_blank_lines=True )
# data2 = pd.read_csv('../data/Run 5/the-mind-is-flat-5_comments.csv', usecols=[0, 1, 2, 5, 9],skip_blank_lines=True )
# data2 = pd.read_csv('../data/Run 6/the-mind-is-flat-6_comments.csv', usecols=[0, 1, 2, 5, 9],skip_blank_lines=True )
# data2 = pd.read_csv('../data/Run 7/the-mind-is-flat-7_comments.csv', usecols=[0, 1, 2, 5, 8],skip_blank_lines=True )
# data2 = pd.read_csv('../data/bigdata/comments.csv', usecols=[0, 1, 2, 5, 8],skip_blank_lines=True )
data2 = pd.read_csv('../data/themindisflat/comments.csv', usecols=[0, 1, 2, 5, 7],skip_blank_lines=True )

# Social learners
# SocialLearners = data2[(data2.likes >= 1) | data2.text.notNull()].groupby('author_id').size()
# SocialLearners = data2[(data2.likes >= 1)].groupby('author_id').size()
SocialLearners = data2[(data2.likes >= '1')].groupby('author_id').size()
print(SocialLearners)

# ice breakers
# IceBreakers = data2[(data2.step_number == 1) & ((data2.likes >= 1) | data2.text.notNull())].groupby('author_id').size()
IceBreakers = data2[(data2.step_number == '1') & (data2.likes >= '1')].groupby('author_id').size()
print(IceBreakers)

# Initiator
Initiator = data2[data2.likes >= '1'].groupby('parent_id').size()
print(Initiator)

# Complimentor
Complimentor = data2[data2.likes >= '1'].groupby('author_id').size()
print(Complimentor)

# Replier
Replier = data2.groupby('author_id').size()
print(Replier)

# s=pd.DataFrame([SocialLearners,IceBreakers,Initiator,Complimentor,Replier],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([1152,164,1074,1152,1484],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([670,100,898,670,911],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([283,46,263,283,384],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([708,102,955,708,932],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([1095,254,2242,1095,1289],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
# s=pd.DataFrame([478,76,703,478,576],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
s=pd.DataFrame([2274,430,3901,2274,2788],index=['SocialLearners','IceBreakers','Initiator','Complimentor','Replier'])
s.plot(kind='bar')
plt.xticks(np.arange(5),('SocialLearners','IceBreakers','Initiator','Complimentor','Replier'),rotation=27)
plt.xlabel('label')
plt.ylabel('')
plt.legend(['label2'])
plt.show()