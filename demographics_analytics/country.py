import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## 国家
data = pd.read_csv('../data/big-data-1_enrolments.csv',usecols=[7])
grouped = data.groupby('country')
#print(grouped.describe())

Unknown = data[(data.country == 'Unknown')].count()
AU = data[(data.country == 'AU')].count()
BR = data[(data.country == 'BR')].count()
CA = data[(data.country == 'CA')].count()
DE = data[(data.country == 'DE')].count()
ES = data[(data.country == 'ES')].count()
FR = data[(data.country == 'FR')].count()
GB = data[(data.country == 'GB')].count()
RU = data[(data.country == 'RU')].count()
UA = data[(data.country == 'UA')].count()
US = data[(data.country == 'US')].count()

s=pd.DataFrame([AU,BR,CA,DE,ES,FR,GB,RU,UA,US],index=['AU','BR','CA','DE','ES','FR','GB','RU','UA','US'])
s.plot(kind='bar')
plt.xticks(np.arange(10),('AU','BR','CA','DE','ES','FR','GB','RU','UA','US'),rotation=27)
plt.xlabel('country')
plt.ylabel('')
plt.show();
