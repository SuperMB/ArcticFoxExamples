
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Pizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Compare two dataframes to see if their content is identical
# Use defaults to compare the most recent two dataframes
# Seed being used: #> DataframesEqual 
# ******************************************************
# ******************************************************

#> Visualize 

pizzeriasCloneDf = #> DataframeCopy 

#> DataframesEqual 

#> print 



# Example 2
# Compare two dataframes to see if their content is identical
# However, this time they do not have equal contents
# Seed being used: #> DataframesEqual 
# ******************************************************
# ******************************************************

# Focus on the original dataframe
#> Focus pizzeriasDf 

#> Visualize 

modifiedDf = #> DataframeCopy 
#> ColumnRemove 5 --throughLastColumn 

#> Visualize 

#> DataframesEqual 

#> print 



