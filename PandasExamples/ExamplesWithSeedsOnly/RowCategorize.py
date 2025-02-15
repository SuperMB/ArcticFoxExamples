
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Weather.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Categorize each row based on MaxTemp, use a default case
# of hot on the high end of the categories, such that
# anything not covered by the conditions (greater than 30)
# will be categorized as hot
# Seed being used: #> RowCategorize MaxTemp --categories cold < 10, cool < 20, warm < 30, hot 
# ******************************************************
# ******************************************************

#> Visualize 


#> ColumnQuantile MaxTemp --quantile .25 .5 .75 1 --print 

#> RowCategorize MaxTemp --categories cold < 10, cool < 20, warm < 30, hot < 40 

#> ColumnRearrange MaxTempCategorized MaxTemp 

#> Visualize 



# Example 2
# Categorize each row based on MaxTemp, use a default case
# of cold on the low end of the categories, such that
# anything not covered by the conditions (less than 10)
# will be categorized as cold
# Seed being used: #> RowCategorize MaxTemp --categories newCold, newCool > 10, newWarm > 20, newHot > 30 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data weather.csv 

#> Visualize 

#> RowCategorize MaxTemp --categories newCold, newCool > 10, newWarm > 20, newHot > 30 

#> ColumnRearrange MaxTempCategorized MaxTemp 

#> Visualize 




