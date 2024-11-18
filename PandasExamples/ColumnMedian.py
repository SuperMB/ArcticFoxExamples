#>1
import pandas as pd
import numpy as np#<1
#⮞ Data Weather.csv ⮜#@>2
weatherDf = pd.read_csv('../Weather.csv')#<2

#⮞ ColumnHeaders ⮜#@>3
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

# Example 1: Calculates Column Median with multiple columns
#⮞ ColumnMedian Evaporation Rainfall Cloud9am --print ⮜#@>4
weatherDfMedian = weatherDf [ ['Evaporation', 'Rainfall', 'Cloud9am'] ].median()
print(weatherDfMedian) ##1#<4

# Example 2: Calculates Column Median with single column
#⮞ ColumnMedian Pressure3pm --print ⮜#@>5
weatherDfMedian = weatherDf['Pressure3pm'].median()
print(weatherDfMedian) ##2#<5
