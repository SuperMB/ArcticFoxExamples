 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 



# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 

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
# Shuffle a dataframe, the original dataframe is shuffled inplace
# Seed being used: #> DataframeShuffle 
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

#> DataframeShuffle --example 
weatherDf = weatherDf.sample(frac=1).reset_index(drop=True) 

#> Visualize 
print(weatherDf.head()) #)2 
##***    MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  WindGustSpeed WindDir9am WindDir3pm  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm RainToday  RISK_MM RainTomorrow
##*** 0     13.3     31.7       0.2          7.8      11.0         WNW           44.0        ESE        WSW           6.0            28           80           23       1021.6       1017.6         2         5     17.5     30.7        No      0.0           No
##*** 1     14.4     24.3       0.0          9.4      11.1         WNW           52.0         NW         NW          31.0            30           36           25       1010.5       1009.9         1         1     20.4     23.0        No      0.0           No
##*** 2      4.6     14.7       0.0          4.4       8.4         WNW           52.0        WNW         NW          28.0            33           54           51       1014.7       1012.4         1         3      9.2     12.0        No      0.0           No
##*** 3     -0.2     18.1       0.0          4.4       9.4          NW           24.0        NaN         NW           0.0             9           80           44       1021.4       1018.9         1         1      6.7     16.9        No      0.0           No
##*** 4      9.6     18.8       0.0          6.4      10.0         WNW           57.0         NW          W          19.0            26           54           42       1012.7       1013.0         2         5     13.1     16.5        No      0.0           No


