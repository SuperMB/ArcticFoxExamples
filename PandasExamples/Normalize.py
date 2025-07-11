 
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
# Seed being used: #> Normalize --all --minMax 
# ******************************************************
# ******************************************************

#> Visualize 
print(appleStockDf.head()) #)1 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Normalize --all --minMax --example 
minMaxScaler = MinMaxScaler()
for column in appleStockDf.columns:
    if is_numeric_dtype(appleStockDf[column]):
        appleStockDf[column] = minMaxScaler.fit_transform(appleStockDf[ [column] ]) 

#> Visualize 
print(appleStockDf.head()) #)2 
##***    Unnamed: 0       Date      Open      High       Low     Close    Volume
##*** 0    0.000000 1980-12-12  0.000257  0.000258  0.000262  0.000261  0.063198
##*** 1    0.000091 1980-12-15  0.000237  0.000236  0.000240  0.000239  0.023699
##*** 2    0.000182 1980-12-16  0.000208  0.000207  0.000211  0.000209  0.014246
##*** 3    0.000273 1980-12-17  0.000215  0.000216  0.000220  0.000219  0.011647
##*** 4    0.000364 1980-12-18  0.000226  0.000227  0.000231  0.000230  0.009897



# Example 2
# Normalize only specified columns
# Seed being used: #> Normalize --columns High Low --minMax 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)3 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Normalize --columns High Low --minMax --example 
scaleColumn = appleStockDf[ ['High', 'Low'] ]
scaleColumn = minMaxScaler.fit_transform(scaleColumn)
appleStockDf[ ['High', 'Low'] ] = scaleColumn 

#> Visualize 
print(appleStockDf.head()) #)4 



# Example 3
# Normalize specified columns with a where condition
# Seed being used: #> Normalize --columns Open  --minMax --where _High_ > 100 
# ******************************************************
# ******************************************************


# Reset original dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)5 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600

#> Normalize --columns Open  --minMax --where _High_ > 100 --example 
scaleColumn = appleStockDf[ ['Open'] ][appleStockDf['High'] > 100]
scaleColumn = minMaxScaler.fit_transform(scaleColumn)
appleStockDf.loc[appleStockDf['High'] > 100,'Open'] = scaleColumn 

#> Visualize 
print(appleStockDf.head()) #)6 
