
import pandas as pd
import numpy as np

#> Data weather.csv 
weatherDf = pd.read_csv('weather.csv') 
weatherDf = pd.read_csv('../weather.csv')

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

# Example 1: Calculates Column Min with multiple columns
#> ColumnMin Humidity3pm Humidity9am Temp3pm --print 
weatherDfMin = weatherDf [ ['Humidity3pm', 'Humidity9am', 'Temp3pm'] ].min()
print(weatherDfMin) #)1 
weatherDfMin = weatherDf [ ['Humidity3pm', 'Humidity9am', 'Temp3pm'] ].min()
print(weatherDfMin) ##1

# Example 2: Calculates Column Min with single column
#> ColumnMin WindGustSpeed --print 
weatherDfMin = weatherDf['WindGustSpeed'].min()
print(weatherDfMin) #)2 
weatherDfMin = weatherDf['WindGustSpeed'].min()
print(weatherDfMin) ##2
