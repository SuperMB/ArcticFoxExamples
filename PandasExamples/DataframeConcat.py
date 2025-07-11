 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 




# Setup
# ******************************************************
# ******************************************************



# Example 1
# Concatenate two dataframes, create a new dataframe with the
# rows from the first dataframe followed by rows from the
# second dataframe
# Seed being used: #> DataframeConcat df2021_FinalDf df2020_FinalDf 
# ******************************************************
# ******************************************************

#> Data 2021_Final.csv 
df2021_FinalDf = pd.read_csv('2021_Final.csv') 

#> Data 2020_Final.csv 
df2020_FinalDf = pd.read_csv('2020_Final.csv') 


#> DataframeConcat df2021_FinalDf df2020_FinalDf --example 
dfsList = [df2021_FinalDf, df2020_FinalDf]
dfsConcat = pd.concat(dfsList, ignore_index=True) 


#> Visualize 
print(dfsConcat.head()) #)1 
##***    YEAR  MONTH STATE               TYPE OF PRODUCER               ENERGY SOURCE  GENERATION\r\n(Megawatthours)
##*** 0  2021      1    AK  Total Electric Power Industry                       Total                         593896
##*** 1  2021      1    AK  Total Electric Power Industry                        Coal                          72164
##*** 2  2021      1    AK  Total Electric Power Industry  Hydroelectric Conventional                         171307
##*** 3  2021      1    AK  Total Electric Power Industry                 Natural Gas                         266928
##*** 4  2021      1    AK  Total Electric Power Industry                       Other                           -318

