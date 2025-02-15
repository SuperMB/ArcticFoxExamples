
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Pizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Get the row at an index
# Seed being used: #> RowGet --index 10 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowGet --index 10 

#> print 



# Example 2
# Get rows within a range
# Seed being used: #> RowGet --indexStart 20 --indexStop 30 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowGet --indexStart 20 --indexStop 30 

#> print 



# Example 3
# Get rows after an index
# Seed being used: #> RowGet --indexStart 200 
# ******************************************************
# ******************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 

#> Visualize 

#> RowGet --indexStart 200 

#> print 



# Example 4
# Get rows before an index
# Seed being used: #> RowGet --indexStop 30 
# ******************************************************
# *****************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 

#> Visualize 

#> RowGet --indexStop 30 

#> print 



# Example 5
# Get rows that meet a criteria
# Seed being used: #> RowGet --where _Location_ contains Queens 
# ******************************************************
# *****************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 

#> Visualize 

#> RowGet --where _Location_ contains Queens 

#> print 


