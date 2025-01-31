
import pandas as pd
import numpy as np
#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 
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

# Example 1: Variance with multiple columns
#> ColumnVariance  WindSpeed3pm Evaporation --print 
weatherDfVar = weatherDf [ ['WindSpeed3pm', 'Evaporation'] ].var()
print(weatherDfVar) #)1 
weatherDfVar = weatherDf [ ['WindSpeed3pm', 'Evaporation'] ].var()
print(weatherDfVar) #)1
weatherDfVar = weatherDf [ ['WindSpeed3pm', 'Evaporation'] ].var()
print(weatherDfVar) ##1

# Example 2: Variance with single columns
#> ColumnVariance  RISK_MM --print 
weatherDfVar = weatherDf['RISK_MM'].var()
print(weatherDfVar) #)2 
weatherDfVar = weatherDf['RISK_MM'].var()
print(weatherDfVar) #)2
weatherDfVar = weatherDf['RISK_MM'].var()
print(weatherDfVar) ##2
