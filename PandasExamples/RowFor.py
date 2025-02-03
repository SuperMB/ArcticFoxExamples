
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
# Iterate over the rows to find the max difference between
# the High and Low columns. RowFor creates the for loop that
# iterates over the rows, the rest of the code in the for loop
# is written by the user, not Arctic Fox. 
# Seed being used: #> RowFor 
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

maxDifference = -100000
#> RowFor 
# User changes detected
for index, row in appleStockDf.iterrows(): 
    maxDifference = max(maxDifference, row['High'] - row['Low'])

#> print 
print(maxDifference) #)2 
##*** 13.529998779296847



