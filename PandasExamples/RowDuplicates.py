 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 





# Setup
# ******************************************************
# ******************************************************

#> RandomDataFrame --columnCount 3 
dfRandomData = {    
    'Column1': np.random.randint(1, 101, size=10000),    
    'Column2': np.random.randint(1, 101, size=10000),    
    'Column3': np.random.randint(1, 101, size=10000),
}

df = pd.DataFrame(dfRandomData) 

#> ColumnHeaders 
# Column1
# Column2
# Column3 



# Example 1
# Count the number of duplicate rows
# Seed being used: #> RowDuplicates --count 
# ******************************************************
# ******************************************************

#> Visualize 
print(df.head()) #)1 
##***    Column1  Column2  Column3
##*** 0       49       39       41
##*** 1       45       84       31
##*** 2       82       19       89
##*** 3       97       11       65
##*** 4       88       10       13


#> RowDuplicates --count --example 
duplicateRowsCount = df[df.duplicated()].shape[0] 

#> print 
print(duplicateRowsCount) #)2 
##*** 49



# Example 2
# Get the duplicate rows
# Seed being used: #> RowDuplicates --count 
# ******************************************************
# ******************************************************

#> Visualize 
print(df.head()) #)3 
##***    Column1  Column2  Column3
##*** 0       49       39       41
##*** 1       45       84       31
##*** 2       82       19       89
##*** 3       97       11       65
##*** 4       88       10       13

#> RowDuplicates --example 
duplicateRows = df[df.duplicated()] 

#> print 
print(duplicateRows) #)4 
##***       Column1  Column2  Column3
##*** 2582       82       69       96
##*** 3298       80       33       19
##*** 3601       30       50       68
##*** 3829       10       60       52
##*** 3920       50       18       51
##*** 4403       25       54       31
##*** 4571       22      100       82
##*** 4686       33      100       75
##*** 4783       56       46       56
##*** 4931      100       81       92
##*** 5075       64       24       85
##*** 5101        2       16       89
##*** 5156       93       16       82
##*** 5208       90       79       91
##*** 5312       66       12       72
##*** 5945       63       79       43
##*** 6139       92       68       68
##*** 6701       93        9       47
##*** 6709       28       27       57
##*** 6941        2       40       45
##*** 7123       93       73       91
##*** 7125       60       96       77
##*** 7467       88       22       29
##*** 7468       60       14        9
##*** 7497        1       22        7
##*** 7528       96       35       89
##*** 7600       72       18       84
##*** 7740       12      100       36
##*** 7897       43       36       17
##*** 7906       71       46       53
##*** 7983       46       30       54
##*** 8073       29       41       59
##*** 8094       87        7       37
##*** 8134       21       52       99
##*** 8295       41       40       81
##*** 8336       57       25       47
##*** 8393       90       90       29
##*** 8481       87       65       36
##*** 8611       48       71       41
##*** 8803       21       53        5
##*** 8913        9       25       23
##*** 8949       87       90       28
##*** 8991       66       12       81
##*** 9249       57       47       78
##*** 9313       10       53      100
##*** 9578        9       97       42
##*** 9681       71       86       58
##*** 9684       94       30       87
##*** 9928        8       27       59



# Example 3
# Remove the duplicate rows
# Seed being used: #> RowDuplicates --remove 
# ******************************************************
# ******************************************************

#> Visualize 
print(duplicateRows.head()) #)5 
##***       Column1  Column2  Column3
##*** 2582       82       69       96
##*** 3298       80       33       19
##*** 3601       30       50       68
##*** 3829       10       60       52
##*** 3920       50       18       51

#> RowCount --print 
duplicateRowsRowCount = duplicateRows.shape[0]
print(duplicateRowsRowCount) #)6 
##*** 49

#> RowDuplicates --remove --example 
duplicateRows = duplicateRows.drop_duplicates(keep='first') 

#> RowCount --print 
duplicateRowsRowCount_1 = duplicateRows.shape[0]
print(duplicateRowsRowCount_1) #)7 
##*** 49

#> Visualize 
print(duplicateRows.head()) #)8 
##***       Column1  Column2  Column3
##*** 2582       82       69       96
##*** 3298       80       33       19
##*** 3601       30       50       68
##*** 3829       10       60       52
##*** 3920       50       18       51

