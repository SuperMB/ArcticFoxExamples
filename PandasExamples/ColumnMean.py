
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

# Example 2: Calculates Column Mean with single column
#> ColumnMean Temp3pm 
weatherDfMean = weatherDf['Temp3pm'].mean() 
weatherDfMean = weatherDf['Temp3pm'].mean()

# Example 1: Calculates Column Mean with multiple columns
#> ColumnMean Temp3pm Temp9am MaxTemp MinTemp 
weatherDfMean = weatherDf [ ['Temp3pm', 'Temp9am', 'MaxTemp', 'MinTemp'] ].mean() 
weatherDfMean = weatherDf [ ['Temp3pm', 'Temp9am', 'MaxTemp', 'MinTemp'] ].mean()


#> print 
print(weatherDfMean) #)1 
print(weatherDfMean) ##1


#> Data Power.csv 
#ISSUE: Can't find Power.csv in the Arctic Fox project. Arctic Fox searched all sub-directories of the project. Please make sure Power.csv is inside the project directories. 
powerDf = pd.read_csv('../Power.csv')

# Does not work
# #> ColumnMean GENERATION  Megawatthours --group STATE TYPE  OF  PRODUCER --addToDataframe --where _STATE_ == AK or _STATE_ == AL --print 

# Does not work
# #> ColumnMean GENERATION  Megawatthours --addToDataframe --where _STATE_ == AK 
