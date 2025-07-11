 
import pandas as pd
import numpy as np  
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
# Get the correlation of all numeric columns in the dataframe
# Seed being used: #> ColumnCorrelation 
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

#> ColumnCorrelation --example 
appleStockDfNumericOnly = appleStockDf.select_dtypes(include=['number'])
appleStockDfCorrelation = appleStockDfNumericOnly.corr() 

#> print 
print(appleStockDfCorrelation) #)2 
##***             Unnamed: 0      Open      High       Low     Close    Volume
##*** Unnamed: 0    1.000000  0.665171  0.665149  0.665085  0.665106  0.091221
##*** Open          0.665171  1.000000  0.999945  0.999942  0.999874 -0.255215
##*** High          0.665149  0.999945  1.000000  0.999926  0.999942 -0.254868
##*** Low           0.665085  0.999942  0.999926  1.000000  0.999942 -0.255743
##*** Close         0.665106  0.999874  0.999942  0.999942  1.000000 -0.255317
##*** Volume        0.091221 -0.255215 -0.254868 -0.255743 -0.255317  1.000000



# Example 2
# Get the correlation of specific columns in the dataframe
# Seed being used: #> ColumnCorrelation --columns High Low Volume 
# ******************************************************
# ******************************************************

# Focus on the original dataframe, not the correlation dataframe
#> Focus appleStockDf 
# Setting focus to appleStockDf 

#> Visualize 
print(appleStockDf.head()) #)3 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> ColumnCorrelation --columns High Low Volume --example 
appleStockDfCorrelation = appleStockDf[ ['High', 'Low', 'Volume'] ].corr() 

#> print 
print(appleStockDfCorrelation) #)4 
##***             High       Low    Volume
##*** High    1.000000  0.999926 -0.254868
##*** Low     0.999926  1.000000 -0.255743
##*** Volume -0.254868 -0.255743  1.000000



# Example 3
# Get the correlation of specific columns in the dataframe
# that meet a given condition
# Seed being used: #> ColumnCorrelation --columns High Low Volume --where _High_ > 1.10 * _Open_ 
# ******************************************************
# ******************************************************

#> Focus appleStockDf 
# Setting focus to appleStockDf 

#> Visualize 
print(appleStockDf.head()) #)5 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> ColumnCorrelation --columns High Low Volume --where _High_ > 1.10 * _Open_  --example 
appleStockDfCorrelation = appleStockDf[ ['High', 'Low', 'Volume'] ][appleStockDf['High'] > 1.10 * appleStockDf['Open']].corr() 

#> print 
print(appleStockDfCorrelation) #)6 
##***             High       Low    Volume
##*** High    1.000000  0.999958  0.057513
##*** Low     0.999958  1.000000  0.061362
##*** Volume  0.057513  0.061362  1.000000
