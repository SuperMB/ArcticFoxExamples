 
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
# Sort the rows on a column with default sorting
# Seed being used: #> RowSort --columns High 
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


#> RowSort --columns High --exampleTitle Sort Dataframe by Single Column --example We often want to sort a dataframe according to the values in a column. To sort by a single column, simply pass in the column name. If the direction, ascending or descending, is not specified, as in this example, the default direction will be ascending, going from smalles to largest. 
appleStockDf = appleStockDf.sort_values(by='High') 

#> Visualize 
print(appleStockDf.head()) #)2 
##***      Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 395         395 1982-07-08  0.038331  0.038331  0.037900  0.037900  164326400
##*** 396         396 1982-07-09  0.039192  0.039623  0.039192  0.039192  128419200
##*** 393         393 1982-07-06  0.040054  0.040054  0.039623  0.039623   87696000
##*** 394         394 1982-07-07  0.039623  0.040054  0.039623  0.039623   30374400
##*** 397         397 1982-07-12  0.040054  0.040484  0.040054  0.040054   63392000



# Example 2
# Sort the rows on a column and specify the order
# Seed being used: #> RowSort --columns Volume --order descending 
# ******************************************************
# ******************************************************

# Reset the dataframe
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

#> RowSort --columns Volume --order descending -exampleTitle Sort by Single Column and Specify Direction --example Similar to the previous, this example sorts the dataframe on a single column. However, this time we specify the order in which to sort, which is descending in this case. This causes the column to be sorted from largest to smallest.
appleStockDf = appleStockDf.sort_values(by='Volume', ascending=False) 

#> Visualize 
print(appleStockDf.head()) #)4 
##***       Unnamed: 0       Date      Open      High       Low     Close      Volume
##*** 5004        5004 2000-09-29  0.425557  0.437824  0.383096  0.388757  7421640800
##*** 4209        4209 1997-08-06  0.190604  0.209476  0.188717  0.198625  4190480000
##*** 4210        4210 1997-08-07  0.217024  0.223158  0.214194  0.220327  3755438400
##*** 6840        6840 2008-01-23  4.112222  4.227263  3.808764  4.199183  3372969600
##*** 4744        4744 1999-09-21  0.552470  0.552941  0.520859  0.522747  3357558400



# Example 3
# Sort the rows on multiple columns and specify the order
# and one column is specified by column number, not name
# Seed being used: #> RowSort --columns High 4 --order descending ascending 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)5 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> RowSort --columns High 4 --order descending ascending --exampleTitle Sort on Multiple Columns --example Rather than sorting on a single column, it is not uncommon to want to sort first on one column, and then sort on a second column when the values of the first column are the same. In this example, we first sort on the column High, and second, we sort on the column with index 4 when the column High has the same value. Additionally, we specify to sort High in descending order, and then column with index 4 in ascending order.
appleStockDf = appleStockDf.sort_values(by= ['High', appleStockDf.columns[4]] , ascending=[False, True]) 

#> Visualize 
print(appleStockDf.head()) #)6 
##***        Unnamed: 0       Date        Open        High         Low       Close    Volume
##*** 10986       10986 2024-07-15  236.531998  237.229996  233.089996  234.399994  58409071
##*** 10983       10983 2024-07-10  229.300003  233.080002  229.250000  232.979996  62627700
##*** 10985       10985 2024-07-12  228.919998  232.639999  228.679993  230.539993  53008200
##*** 10984       10984 2024-07-11  231.389999  232.389999  225.770004  227.570007  64710600
##*** 10982       10982 2024-07-09  227.929993  229.399994  226.369995  228.679993  48076100
