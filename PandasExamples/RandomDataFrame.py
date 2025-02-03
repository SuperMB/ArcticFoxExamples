
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
# Default random data frame, useful for quickly testing
# some functionality where you need a dataframe but do
# not want to search for data
# Seed being used: #> RandomDataFrame 
# ******************************************************
# ******************************************************

#> RandomDataFrame 
dfRandomData = {    
    'Column1': np.random.randint(1, 101, size=10000),    
    'Column2': np.random.randint(1, 101, size=10000),    
    'Column3': np.random.randint(1, 101, size=10000),    
    'Column4': np.random.randint(1, 101, size=10000),    
    'Column5': np.random.randint(1, 101, size=10000),    
    'Column6': np.random.randint(1, 101, size=10000),    
    'Column7': np.random.randint(1, 101, size=10000),    
    'Column8': np.random.randint(1, 101, size=10000),    
    'Column9': np.random.randint(1, 101, size=10000),    
    'Column10': np.random.randint(1, 101, size=10000),
}

df = pd.DataFrame(dfRandomData) 

#> Visualize 
print(df.head()) #)1 

##*** 0       14       70       95       97       53       79       15       44       56        49
##*** 1       44       14       80        7        3       30       53       72       48        90
##*** 2       26       23       20       18       97       52       87        3       78        39
##*** 3       19       57       29        7       64       73       81       26       58        62
##*** 4       68       83       59       40       76       88       72      100       11        65



# Example 2
# A random data frame, but you specify some of the size
# and shape parameters of the dataframe
# Seed being used: #> RandomDataFrame --columnCount 3 --rowCount 10 
# ******************************************************
# ******************************************************

#> RandomDataFrame --columnCount 3 --rowCount 10 
dfRandomData_1 = {    
    'Column1': np.random.randint(1, 101, size=10),    
    'Column2': np.random.randint(1, 101, size=10),    
    'Column3': np.random.randint(1, 101, size=10),
}

df_1 = pd.DataFrame(dfRandomData_1) 

#> Visualize --count 10 
print(df_1.head(n=10)) #)2 
##***    Column1  Column2  Column3
##*** 0       11       86       18
##*** 1       62       32       30
##*** 2       92       12       75
##*** 3       82       10       10
##*** 4       95        1       58
##*** 5       20       19       94
##*** 6       93        6       30
##*** 7       55       29       95
##*** 8       98       35       99
##*** 9       39       69        8
