
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pandas.api.types import is_numeric_dtype  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

#> ColumnHeaders 
# Unnamed
# Date
# Open
# High
# Low
# Close
# Volume 



# Example 1
# Normalize the entire dataframe with
# Seed being used: #> ColumnSum  AccountBalance --print 
# ******************************************************
# ******************************************************

#> Visualize 
print(appleStockDf.head()) #)1 

#> Normalize --all --minMax 
minMaxScaler = MinMaxScaler()
for column in appleStockDf.columns:
    if is_numeric_dtype(appleStockDf[column]):
        appleStockDf[column] = minMaxScaler.fit_transform(appleStockDf[ [column] ]) 

#> Visualize 
print(appleStockDf.head()) #)2 




