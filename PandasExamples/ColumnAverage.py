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

#Example 1 Get average of WindGustSpeed and MinTemp
#⮞ ColumnAverage WindGustSpeed MinTemp ⮜#@>4
weatherDfMean = weatherDf [ ['WindGustSpeed', 'MinTemp'] ].mean()#<4
#Example 1 Get average of MaxTemp
#⮞ ColumnAverage MaxTemp ⮜#@>5
weatherDfMean = weatherDf['MaxTemp'].mean()#<5
#Example 1 Get average of Evaporation 
#⮞ ColumnAverage Evaporation ⮜#@>6
weatherDfMean = weatherDf['Evaporation'].mean()#<6



