#>1
import pandas as pd
import numpy as np#<1

#⮞ Data 2021_Final.csv ⮜#@>2
df2021_FinalDf = pd.read_csv('../2021_Final.csv')#<2

#⮞ Data 2020_Final.csv ⮜#@>3
df2020_FinalDf = pd.read_csv('../2020_Final.csv')#<3

#⮞ DataframeConcat df2021_FinalDf df2020_FinalDf ⮜#@>4
dfsList = [df2021_FinalDf, df2020_FinalDf]
dfsConcat = pd.concat(dfsList, ignore_index=True)#<4

