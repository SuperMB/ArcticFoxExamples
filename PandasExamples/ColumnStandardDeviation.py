
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

# Example 1: Standard deviation with multiple columns
#> ColumnStandardDeviation Temp3pm Temp9am Rainfall 
weatherDfStd = weatherDf [ ['Temp3pm', 'Temp9am', 'Rainfall'] ].std() 
weatherDfStd = weatherDf [ ['Temp3pm', 'Temp9am', 'Rainfall'] ].std()
weatherDfStd = weatherDf [ ['Temp3pm', 'Temp9am', 'Rainfall'] ].std()

# Example 2: Standard deviation with single column
#> ColumnStandardDeviation  Humidity3pm --print 
weatherDfStd = weatherDf['Humidity3pm'].std()
print(weatherDfStd) #)1 
weatherDfStd = weatherDf['Humidity3pm'].std()
print(weatherDfStd) #)1
weatherDfStd = weatherDf['Humidity3pm'].std()
print(weatherDfStd) ##1
