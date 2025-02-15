
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Calculate minimum of a single column
# Seed being used: #> ColumnMin WindGustSpeed --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMin WindGustSpeed --print 



# Example 2
# Calculate minimum of multiple columns
# Seed being used: #> ColumnMin Humidity3pm Humidity9am Temp3pm --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMin Humidity3pm Humidity9am Temp3pm --print 



# Example 3
# Calculate column mean of a column on a sliding window of the last 3 readings, and
# grouped by another column, and add the result back into the dataframe as a new column
# Seed being used: #> ColumnMean --columns Sunshine --rolling 7 --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMin --columns Sunshine --rolling 3 --group WindGustDir --addToDataframe 

#> Focus weatherDf 

#> Visualize --count 30 



