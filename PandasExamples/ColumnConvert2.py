#>1
import pandas as pd
import numpy as np
#<1 #>2
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)#<2

#⮞ Data weather.csv ⮜#@>3
weatherDf = pd.read_csv('../weather.csv')#<3

#⮞ ColumnHeaders ⮜#@>4
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
# RainTomorrow#<4

#⮞ VisualizeAllColumns  ⮜#@>5
# Code added to start of file to display all columns for dataframes#<5

#MB Rafactor
#⮞ ColumnConvert   --columns MaxTemp --from celsius --to fahrenheit  ⮜#@8#@>6
weatherDf['MaxTemp'] = weatherDf['MaxTemp'] * 9/5 + 32
weatherDf['MaxTemp'] = Unsupported unit celsius.#<6

#⮞ print  ⮜#@>7
print(weatherDf) ##1#<7


