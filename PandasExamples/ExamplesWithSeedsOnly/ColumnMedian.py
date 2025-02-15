
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Calculate median of a single column, and print result to file
# Seed being used: #> ColumnMedian Pressure3pm --print 
# ******************************************************
# ******************************************************

#> Visualize 

# Example 2: Calculates Column Median with single column
#> ColumnMedian Pressure3pm --print 



# Example 2
# Calculate median of multiple columns
# Seed being used: #> ColumnMedian Evaporation Rainfall Cloud9am --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMedian Evaporation Rainfall Cloud9am --print 



# Example 3
# Calculate column mean of a column, grouped by the categories of a different column,
# and add the result to the dataframe
# Seed being used: #> ColumnMedian --columns Sunshine --group WindGustDir --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMedian --columns Sunshine --group WindGustDir --addToDataframe 

#> Visualize --count 20 



