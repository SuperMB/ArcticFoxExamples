
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

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



# Example 1
# Variance with single columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(weatherDf.head()) #)1 

#> ColumnVariance  RISK_MM --print 
weatherDfVar = weatherDf['RISK_MM'].var()
print(weatherDfVar) #)2 



# Example 2
# Variance with multiple columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(weatherDf.head()) #)3 

#> ColumnVariance  WindSpeed3pm Evaporation --print 
weatherDfVar = weatherDf [ ['WindSpeed3pm', 'Evaporation'] ].var()
print(weatherDfVar) #)4 



