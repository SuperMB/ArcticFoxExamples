
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




# Example
# Standard deviation with single column
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(weatherDf.head()) #)1 

#> ColumnStandardDeviation  Humidity3pm 
weatherDfStd = weatherDf['Humidity3pm'].std() 

#> print 
print(weatherDfStd) #)2 



# Example
# Standard deviation with multiple columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(weatherDf.head()) #)3 

#> ColumnStandardDeviation Temp3pm Temp9am Rainfall 
weatherDfStd = weatherDf [ ['Temp3pm', 'Temp9am', 'Rainfall'] ].std() 

#> print 
print(weatherDfStd) #)4 
