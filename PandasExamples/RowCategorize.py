
import sys
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

#> ColumnHeaders 
# MinTemp
# MaxTemp
# Rainfall
# Evaporation
# Sunshine
# WindGustDir
# WindGustSpeed
# WindDir9am
# WindDir3pm
# WindSpeed9am
# WindSpeed3pm
# Humidity9am
# Humidity3pm
# Pressure9am
# Pressure3pm
# Cloud9am
# Cloud3pm
# Temp9am
# Temp3pm
# RainToday
# RISK_MM
# RainTomorrow 



# Example 1
# Categorize each row based on MaxTemp, use a default case
# of hot on the high end of the categories, such that
# anything not covered by the conditions (greater than 30)
# will be categorized as hot
# Seed being used: #> RowCategorize MaxTemp --categories cold < 10, cool < 20, warm < 30, hot 
# ******************************************************
# ******************************************************

#> Visualize 
print(weatherDf.head()) #)1 
##***    MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  WindGustSpeed WindDir9am WindDir3pm  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm RainToday  RISK_MM RainTomorrow
##*** 0      8.0     24.3       0.0          3.4       6.3          NW           30.0         SW         NW           6.0            20           68           29       1019.7       1015.0         7         7     14.4     23.6        No      3.6          Yes
##*** 1     14.0     26.9       3.6          4.4       9.7         ENE           39.0          E          W           4.0            17           80           36       1012.4       1008.4         5         3     17.5     25.7       Yes      3.6          Yes
##*** 2     13.7     23.4       3.6          5.8       3.3          NW           85.0          N        NNE           6.0             6           82           69       1009.5       1007.2         8         7     15.4     20.2       Yes     39.8          Yes
##*** 3     13.3     15.5      39.8          7.2       9.1          NW           54.0        WNW          W          30.0            24           62           56       1005.5       1007.0         2         7     13.5     14.1       Yes      2.8          Yes
##*** 4      7.6     16.1       2.8          5.6      10.6         SSE           50.0        SSE        ESE          20.0            28           68           49       1018.3       1018.5         7         7     11.1     15.4       Yes      0.0           No


#> ColumnQuantile MaxTemp --quantile .25 .5 .75 1 --print 
weatherDfQuantile = weatherDf['MaxTemp'].quantile( [ .25, .5, .75, 1 ] )
print(weatherDfQuantile) #)2 
##*** 0.25    15.025
##*** 0.50    19.650
##*** 0.75    25.500
##*** 1.00    35.800
##*** Name: MaxTemp, dtype: float64

#> RowCategorize MaxTemp --categories cold < 10, cool < 20, warm < 30, hot < 40 
weatherDf['MaxTempCategorized'] = pd.cut(x=weatherDf['MaxTemp'], bins=[-sys.float_info.max,10,20,30,40], labels=['cold','cool','warm','hot'], include_lowest=True) 

#> ColumnRearrange MaxTempCategorized MaxTemp 
columnsToMove = ['MaxTempCategorized', 'MaxTemp']
columnsToMove = columnsToMove + [column for column in weatherDf.columns if column not in columnsToMove]
weatherDf = weatherDf[columnsToMove] 

#> Visualize 
print(weatherDf.head()) #)3 
##***   MaxTempCategorized  MaxTemp  MinTemp  Rainfall  Evaporation  Sunshine WindGustDir  WindGustSpeed WindDir9am WindDir3pm  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm RainToday  RISK_MM RainTomorrow
##*** 0               warm     24.3      8.0       0.0          3.4       6.3          NW           30.0         SW         NW           6.0            20           68           29       1019.7       1015.0         7         7     14.4     23.6        No      3.6          Yes
##*** 1               warm     26.9     14.0       3.6          4.4       9.7         ENE           39.0          E          W           4.0            17           80           36       1012.4       1008.4         5         3     17.5     25.7       Yes      3.6          Yes
##*** 2               warm     23.4     13.7       3.6          5.8       3.3          NW           85.0          N        NNE           6.0             6           82           69       1009.5       1007.2         8         7     15.4     20.2       Yes     39.8          Yes
##*** 3               cool     15.5     13.3      39.8          7.2       9.1          NW           54.0        WNW          W          30.0            24           62           56       1005.5       1007.0         2         7     13.5     14.1       Yes      2.8          Yes
##*** 4               cool     16.1      7.6       2.8          5.6      10.6         SSE           50.0        SSE        ESE          20.0            28           68           49       1018.3       1018.5         7         7     11.1     15.4       Yes      0.0           No



# Example 2
# Categorize each row based on MaxTemp, use a default case
# of cold on the low end of the categories, such that
# anything not covered by the conditions (less than 10)
# will be categorized as cold
# Seed being used: #> RowCategorize MaxTemp --categories newCold, newCool > 10, newWarm > 20, newHot > 30 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data weather.csv 
weatherDf = pd.read_csv('weather.csv') 

#> Visualize 
print(weatherDf.head()) #)4 

#> RowCategorize MaxTemp --categories newCold, newCool > 10, newWarm > 20, newHot > 30 
weatherDf['MaxTempCategorized'] = pd.cut(x=weatherDf['MaxTemp'], bins=[-sys.float_info.max,sys.float_info.max], labels=['newCold' 'newCool' '>' 10 'newWarm' '>' 20 'newHot' '>' 30], include_lowest=True) 

#> ColumnRearrange MaxTempCategorized MaxTemp 
columnsToMove = ['MaxTempCategorized', 'MaxTemp']
columnsToMove = columnsToMove + [column for column in weatherDf.columns if column not in columnsToMove]
weatherDf = weatherDf[columnsToMove] 

#> Visualize 
print(weatherDf.head()) #)5 

