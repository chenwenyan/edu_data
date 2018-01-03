import pandas as pd
import matplotlib.pyplot as plt

## 国家
data = pd.read_csv('../data/big-data-1_enrolments.csv',usecols=[9])
grouped = data.groupby('highest_education_level')
#print(grouped.describe())

Unknown = data[(data.highest_education_level == 'Unknown')].count()
apprenticeship = data[(data.highest_education_level == 'apprenticeship')].count()
less_than_secondary = data[(data.highest_education_level == 'less_than_secondary')].count()
professional = data[(data.highest_education_level == 'professional')].count()
secondary = data[(data.highest_education_level == 'secondary')].count()
tertiary = data[(data.highest_education_level == 'tertiary')].count()
university_degree = data[(data.highest_education_level == 'university_degree')].count()
university_doctorate = data[(data.highest_education_level == 'university_doctorate')].count()
university_masters = data[(data.highest_education_level == 'university_masters')].count()

s=pd.DataFrame([apprenticeship,less_than_secondary,professional,secondary,tertiary,university_degree,university_doctorate,university_masters],index=['apprenticeship','less_than_secondary','professional','secondary','tertiary','university_degree','university_doctorate','university_masters'])
s.plot(kind='bar')
plt.xlabel('highest_education_level')
plt.ylabel('')
plt.show()
