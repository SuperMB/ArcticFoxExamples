#>1
import pandas as pd
import numpy as np#<1

#⮞ Data weather.csv ⮜#@>2
weatherDf = pd.read_csv('../weather.csv')#<2

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

# Example 1: Calculates Column Min with multiple columns
#⮞ ColumnMin Humidity3pm Humidity9am Temp3pm --print ⮜#@>4
weatherDfMin = weatherDf [ ['Humidity3pm', 'Humidity9am', 'Temp3pm'] ].min()
print(weatherDfMin) ##1#<4

# Example 2: Calculates Column Min with single column
#⮞ ColumnMin WindGustSpeed --print ⮜#@>5
weatherDfMin = weatherDf['WindGustSpeed'].min()
print(weatherDfMin) ##2#<5
