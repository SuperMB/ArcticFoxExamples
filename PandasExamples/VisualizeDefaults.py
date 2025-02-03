
import pandas as pd
import numpy as np 


# Setup
# ******************************************************
# ******************************************************

#> Data weather.csv 
weatherDf = pd.read_csv('weather.csv') 

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
# Sets the default behavior for the visualize seed.
# With the configurations below, VisualizeDefaults makes
# all Visualize seeds in the workspace show all of the columns
# and show 20 rows.
# Seed being used: #> VisualizeDefaults --allColumns --count 20 
# ******************************************************
# ******************************************************

# #> VisualizeDefaults --allColumns --count 20 

#> Visualize 
print(weatherDf.head()) #)1 
##***     MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  WindGustSpeed WindDir9am WindDir3pm  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm RainToday  RISK_MM RainTomorrow
##*** 0       8.0     24.3       0.0          3.4       6.3          NW           30.0         SW         NW           6.0            20           68           29       1019.7       1015.0         7         7     14.4     23.6        No      3.6          Yes
##*** 1      14.0     26.9       3.6          4.4       9.7         ENE           39.0          E          W           4.0            17           80           36       1012.4       1008.4         5         3     17.5     25.7       Yes      3.6          Yes
##*** 2      13.7     23.4       3.6          5.8       3.3          NW           85.0          N        NNE           6.0             6           82           69       1009.5       1007.2         8         7     15.4     20.2       Yes     39.8          Yes
##*** 3      13.3     15.5      39.8          7.2       9.1          NW           54.0        WNW          W          30.0            24           62           56       1005.5       1007.0         2         7     13.5     14.1       Yes      2.8          Yes
##*** 4       7.6     16.1       2.8          5.6      10.6         SSE           50.0        SSE        ESE          20.0            28           68           49       1018.3       1018.5         7         7     11.1     15.4       Yes      0.0           No
##*** 5       6.2     16.9       0.0          5.8       8.2          SE           44.0         SE          E          20.0            24           70           57       1023.8       1021.7         7         5     10.9     14.8        No      0.2           No
##*** 6       6.1     18.2       0.2          4.2       8.4          SE           43.0         SE        ESE          19.0            26           63           47       1024.6       1022.2         4         6     12.4     17.3        No      0.0           No
##*** 7       8.3     17.0       0.0          5.6       4.6           E           41.0         SE          E          11.0            24           65           57       1026.2       1024.2         6         7     12.1     15.5        No      0.0           No
##*** 8       8.8     19.5       0.0          4.0       4.1           S           48.0          E        ENE          19.0            17           70           48       1026.1       1022.7         7         7     14.1     18.9        No     16.2          Yes
##*** 9       8.4     22.8      16.2          5.4       7.7           E           31.0          S        ESE           7.0             6           82           32       1024.1       1020.7         7         1     13.3     21.7       Yes      0.0           No
##*** 10      9.1     25.2       0.0          4.2      11.9           N           30.0         SE         NW           6.0             9           74           34       1024.4       1021.1         1         2     14.6     24.0        No      0.2           No
##*** 11      8.5     27.3       0.2          7.2      12.5           E           41.0          E         NW           2.0            15           54           35       1023.8       1019.9         0         3     16.8     26.0        No      0.0           No
##*** 12     10.1     27.9       0.0          7.2      13.0         WNW           30.0          S         NW           6.0             7           62           29       1022.0       1017.1         0         1     17.0     27.1        No      0.0           No
##*** 13     12.1     30.9       0.0          6.2      12.4          NW           44.0        WNW          W           7.0            20           67           20       1017.3       1013.1         1         4     19.7     30.7        No      0.0           No
##*** 14     10.1     31.2       0.0          8.8      13.1          NW           41.0          S          W           6.0            20           45           16       1018.2       1013.7         0         1     18.7     30.4        No      0.0           No
##*** 15     12.4     32.1       0.0          8.4      11.1           E           46.0         SE        WSW           7.0             9           70           22       1017.9       1012.8         0         3     19.1     30.7        No      0.0           No
##*** 16     13.8     31.2       0.0          7.2       8.4         ESE           44.0        WSW          W           6.0            19           72           23       1014.4       1009.8         7         6     20.2     29.8        No      1.2          Yes
##*** 17     11.7     30.0       1.2          7.2      10.1           S           52.0         SW         NE           6.0            11           59           26       1016.4       1013.0         1         5     20.1     28.6       Yes      0.6           No
##*** 18     12.4     32.3       0.6          7.4      13.0           E           39.0        NNE          W           4.0            17           60           25       1017.1       1013.3         1         3     20.2     31.2        No      0.0           No
##*** 19     15.6     33.4       0.0          8.0      10.4          NE           33.0        NNW        NNW           2.0            13           61           27       1018.5       1013.7         0         1     22.8     32.0        No      0.0           No
