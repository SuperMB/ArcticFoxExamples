
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 



# Example 1
# Description
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Data 2021_Final.csv 
df2021_FinalDf = pd.read_csv('2021_Final.csv') 

#> Data 2020_Final.csv 
df2020_FinalDf = pd.read_csv('2020_Final.csv') 


#> DataframeConcat df2021_FinalDf df2020_FinalDf 
dfsList = [df2021_FinalDf, df2020_FinalDf]
dfsConcat = pd.concat(dfsList, ignore_index=True) 



