
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 




# Example 1
# Get average of a single column, MaxTemp
# Seed being used: #> ColumnAverage MaxTemp --print 
# ******************************************************
# ******************************************************

#> Visualize 
#> ColumnAverage MaxTemp --print 



# Example 2
# Get average of multiple columns, WindGustSpeed, MinTemp, and Evaporation
# Seed being used: #> ColumnAverage WindGustSpeed MinTemp Evaporation --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnAverage WindGustSpeed MinTemp Evaporation --print 



# Example 3
# Get moving window average of Sunshine, averaged over the last 5 readings, and add back to the dataframe
# Seed being used: #> ColumnAverage --columns Sunshine --rolling 5 --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnAverage --columns Sunshine --rolling 5 --addToDataframe 

#> Visualize --count 15 


