
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

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

#> ColumnHeaders 
# Column1
# Column2
# Column3
# Column4
# Column5
# Column6
# Column7
# Column8
# Column9
# Column10 



# Example 1
# Count the number of duplicate rows
# Seed being used: #> RowDuplicates --count 
# ******************************************************
# ******************************************************

#> Visualize 
print(df.head()) #)1 
##***    Column1  Column2  Column3
##*** 0       15       82       60
##*** 1        4       73       26
##*** 2       57       44       12
##*** 3       23        4       55
##*** 4       60       19       80


#> RowDuplicates --count 
duplicateRowsCount = df[df.duplicated()].shape[0] 

#> print 
print(duplicateRowsCount) #)2 
##*** 59



# Example 2
# Get the duplicate rows
# Seed being used: #> RowDuplicates --count 
# ******************************************************
# ******************************************************

#> Visualize 
print(df.head()) #)3 
##***    Column1  Column2  Column3
##*** 0       15       82       60
##*** 1        4       73       26
##*** 2       57       44       12
##*** 3       23        4       55
##*** 4       60       19       80

#> RowDuplicates 
duplicateRows = df[df.duplicated()] 

#> print 
print(duplicateRows) #)4 
##***       Column1  Column2  Column3
##*** 348        13       75       59
##*** 785        77       85       70
##*** 1937       58        5       62
##*** 2220       64       77       21
##*** 2484       19        9       87
##*** 2917       69       85       24
##*** 2931       45       99       67
##*** 3082       32       73       77
##*** 3220       36       20       95
##*** 3487       86       48        9
##*** 3972       30       23       11
##*** 4957       48       76       41
##*** 5281       60       87        4
##*** 5471       98       33       71
##*** 5995       10       91       72
##*** 6041       23       93       30
##*** 6222       84       37       34
##*** 6227       82       52       26
##*** 6244       69       53        5
##*** 6366       72       57       36
##*** 6388      100       99       31
##*** 6495       39       51       34
##*** 6503       84       29       69
##*** 6600       98       66       46
##*** 6646       84       21       42
##*** 7248       82       52       96
##*** 7316       39       92       19
##*** 7320       81        2       97
##*** 7384       64       18       18
##*** 7480       66       77       67
##*** 7495       41       20       64
##*** 7729       65       65       47
##*** 8165        8       18       86
##*** 8206       48       91        8
##*** 8368       89       57       53
##*** 8372       95        6       62
##*** 8380       65       71       83
##*** 8487       89       58       60
##*** 8651       69       92       69
##*** 8663       19       63       42
##*** 8964        3       63       26
##*** 8967       81        6       17
##*** 9112       22       35       31
##*** 9224       65       25       10
##*** 9285       20       48       39
##*** 9301       28       46       78
##*** 9303       45       67      100
##*** 9388       59       25        8
##*** 9395       12       27       86
##*** 9418       11        6       76
##*** 9419       35       15        1
##*** 9449       12       18       70
##*** 9490       83       69       31
##*** 9534       14       48       79
##*** 9574       23       81       33
##*** 9699       41       19       75
##*** 9717       32       71       31
##*** 9878       81       40        7
##*** 9911       69       27       34



# Example 3
# Remove the duplicate rows
# Seed being used: #> RowDuplicates --remove 
# ******************************************************
# ******************************************************

#> Visualize 
print(df.head()) #)5 
##***    Column1  Column2  Column3
##*** 0       15       82       60
##*** 1        4       73       26
##*** 2       57       44       12
##*** 3       23        4       55
##*** 4       60       19       80

#> RowCount --print 
dfRowCount = df.shape[0]
print(dfRowCount) #)6 
##*** 10000

#> RowDuplicates --remove 
df.drop_duplicates(inplace=True) 

#> RowCount --print 
dfRowCount_1 = df.shape[0]
print(dfRowCount_1) #)7 
##*** 9941

#> Visualize 
print(df.head()) #)8 
##***    Column1  Column2  Column3
##*** 0       15       82       60
##*** 1        4       73       26
##*** 2       57       44       12
##*** 3       23        4       55
##*** 4       60       19       80

