import pandas as pd
import pandas_datareader.data as pdd

sym = 'GS'
finace = pdd.DataReader('F-F_Research_Data_factors','famafrench')
print(finace.tail())