
import pandas as pd
import numpy as np

pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)

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

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 
# Code added to start of file to display all columns for dataframes

#MB Rafactor
#> ColumnConvert   --columns MaxTemp --from celsius --to fahrenheit 
weatherDf['MaxTemp'] = weatherDf['MaxTemp'] * 9/5 + 32
weatherDf['MaxTemp'] = Unsupported unit celsius.  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 
weatherDf['MaxTemp'] = weatherDf['MaxTemp'] * 9/5 + 32
weatherDf['MaxTemp'] = Unsupported unit celsius.

#> print 
print(weatherDf) #)1 
print(weatherDf) ##1


