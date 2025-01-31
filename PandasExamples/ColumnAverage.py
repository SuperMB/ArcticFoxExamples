
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

#Example 1 Get average of WindGustSpeed and MinTemp
#> ColumnAverage WindGustSpeed MinTemp 
weatherDfMean = weatherDf [ ['WindGustSpeed', 'MinTemp'] ].mean() 
weatherDfMean = weatherDf [ ['WindGustSpeed', 'MinTemp'] ].mean()
#Example 1 Get average of MaxTemp
#> ColumnAverage MaxTemp 
weatherDfMean = weatherDf['MaxTemp'].mean() 
weatherDfMean = weatherDf['MaxTemp'].mean()
#Example 1 Get average of Evaporation
#> ColumnAverage Evaporation 
weatherDfMean = weatherDf['Evaporation'].mean() 
weatherDfMean = weatherDf['Evaporation'].mean()



