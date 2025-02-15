
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Calculate mean of a single column
# Seed being used: #> ColumnMean Temp3pm 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMean Temp3pm 

#> print 



# Example 2
# Calculate mean of multiple columns
# Seed being used: #> ColumnMean Temp3pm Temp9am MaxTemp MinTemp 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMean Temp3pm Temp9am MaxTemp MinTemp 

#> print 



# Example 3
# Calculate column mean of a column on a sliding window of the last 7 readings, and
# add the result back into the dataframe as a new column
# Seed being used: #> ColumnMean --columns Sunshine --rolling 7 --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMean --columns Sunshine --rolling 7 --addToDataframe 

#> Visualize --count 15 


