
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Get the variance of a single column
# Seed being used: #> ColumnVariance RISK_MM --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnVariance RISK_MM --print 



# Example 2
# Get the variance of multiple columns
# Seed being used: #> ColumnVariance WindSpeed3pm Evaporation --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnVariance WindSpeed3pm Evaporation --print 



# Example 3
# Get the variance of multiple columns grouped
# according to the categorize of another column
# Seed being used: #> ColumnVariance Sunshine Rainfall --group RainTomorrow 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnVariance Sunshine Rainfall --group RainTomorrow --print 

