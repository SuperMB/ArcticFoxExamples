
import pandas as pd
import numpy as np
#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 
weatherDf = pd.read_csv('../Weather.csv')

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

# Example 1: Calculates Column Median with multiple columns
#> ColumnMedian Evaporation Rainfall Cloud9am --print 
weatherDfMedian = weatherDf [ ['Evaporation', 'Rainfall', 'Cloud9am'] ].median()
print(weatherDfMedian) #)1 
weatherDfMedian = weatherDf [ ['Evaporation', 'Rainfall', 'Cloud9am'] ].median()
print(weatherDfMedian) ##1

# Example 2: Calculates Column Median with single column
#> ColumnMedian Pressure3pm --print 
weatherDfMedian = weatherDf['Pressure3pm'].median()
print(weatherDfMedian) #)2 
weatherDfMedian = weatherDf['Pressure3pm'].median()
print(weatherDfMedian) ##2
