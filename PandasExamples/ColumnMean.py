#>1
import pandas as pd
import numpy as np#<1

#⮞ Data weather.csv ⮜#@>2
weatherDf = pd.read_csv('../weather.csv')#<2

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

# Example 2: Calculates Column Mean with single column
#⮞ ColumnMean Temp3pm ⮜#@>4
weatherDfMean = weatherDf['Temp3pm'].mean()#<4

# Example 1: Calculates Column Mean with multiple columns
#⮞ ColumnMean Temp3pm Temp9am MaxTemp MinTemp ⮜#@>5
weatherDfMean = weatherDf [ ['Temp3pm', 'Temp9am', 'MaxTemp', 'MinTemp'] ].mean()#<5


#⮞ print  ⮜#@>6
print(weatherDfMean) ##1#<6


#⮞ Data Power.csv ⮜#@>7
powerDf = pd.read_csv('../Power.csv')#<7

# Does not work
# #⮞ ColumnMean GENERATION  Megawatthours --group STATE TYPE  OF  PRODUCER --addToDataframe --where _STATE_ == AK or _STATE_ == AL --print ⮜#@8

# Does not work
# #⮞ ColumnMean GENERATION  Megawatthours --addToDataframe --where _STATE_ == AK  ⮜#@9
