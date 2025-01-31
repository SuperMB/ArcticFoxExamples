
import pandas as pd
import numpy as np

#> Data 2021_Final.csv 
df2021_FinalDf_1 = pd.read_csv('2021_Final.csv') 
df2021_FinalDf = pd.read_csv('../2021_Final.csv')

#> Data 2020_Final.csv 
df2020_FinalDf_1 = pd.read_csv('2020_Final.csv') 
df2020_FinalDf = pd.read_csv('../2020_Final.csv')

#> DataframeConcat df2021_FinalDf df2020_FinalDf 
dfsList = [df2021_FinalDf, df2020_FinalDf]
dfsConcat = pd.concat(dfsList, ignore_index=True) 
dfsList = [df2021_FinalDf, df2020_FinalDf]
dfsConcat = pd.concat(dfsList, ignore_index=True)

