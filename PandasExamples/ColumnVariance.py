#>1
import pandas as pd
import numpy as np#<1
#⮞ Data Weather.csv ⮜#@>2
weatherDf = pd.read_csv('../Weather.csv')#<2

#⮞ ColumnHeaders  ⮜#@>3
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
# RainTomorrow#<3

# Example 1: Variance with multiple columns
#⮞ ColumnVariance  WindSpeed3pm Evaporation --print ⮜ #⮞ `> ⮜#@>4
weatherDfVar = weatherDf [ ['WindSpeed3pm', 'Evaporation'] ].var()
print(weatherDfVar) ##1#<4

# Example 2: Variance with single columns
#⮞ ColumnVariance  RISK_MM --print ⮜#@>5
weatherDfVar = weatherDf['RISK_MM'].var()
print(weatherDfVar) ##2#<5
