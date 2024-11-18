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

# Example 1: Standard deviation with multiple columns
#⮞ ColumnStandardDeviation Temp3pm Temp9am Rainfall ⮜#@>4
weatherDfStd = weatherDf [ ['Temp3pm', 'Temp9am', 'Rainfall'] ].std()#<4

# Example 2: Standard deviation with single column
#⮞ ColumnStandardDeviation  Humidity3pm --print ⮜#@>5
weatherDfStd = weatherDf['Humidity3pm'].std()
print(weatherDfStd) ##1#<5
