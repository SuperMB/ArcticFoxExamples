

#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Calculate mode of a single column
# Seed being used: #> ColumnMode Cloud3pm --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMode Cloud3pm --print 



# Example 2
# Calculate mode of multiple columns
# Seed being used: #> ColumnMode Humidity3pm Humidity9am Temp3pm --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMode Humidity3pm Humidity9am Temp3pm --print 



# Example 3
# Calculate column mean of a column, grouped by the categories of a different column,
# and add the result to the dataframe
# Seed being used: #> ColumnMode --columns MaxTemp --group RainToday --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMode --columns MaxTemp --group RainToday --addToDataframe 

#> Visualize --count 10 


