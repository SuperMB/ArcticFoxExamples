
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

# Example 1: Calculates Column Mode with multiple columns
#> ColumnMode Humidity3pm Humidity9am Temp3pm --print 
weatherDfMode = weatherDf [ ['Humidity3pm', 'Humidity9am', 'Temp3pm'] ].mode()
print(weatherDfMode) #)1 
weatherDfMode = weatherDf [ ['Humidity3pm', 'Humidity9am', 'Temp3pm'] ].mode()
print(weatherDfMode) ##1

# Example 2: Calculates Column Mode with single column
#> ColumnMode Cloud3pm --print 
weatherDfMode = weatherDf['Cloud3pm'].mode()
print(weatherDfMode) #)2 
weatherDfMode = weatherDf['Cloud3pm'].mode()
print(weatherDfMode) ##2
