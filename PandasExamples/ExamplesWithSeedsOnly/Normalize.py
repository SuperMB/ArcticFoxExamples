
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Normalize the entire dataframe with
# Seed being used: #> Normalize --all --minMax 
# ******************************************************
# ******************************************************

#> Visualize 

#> Normalize --all --minMax 

#> Visualize 



# Example 2
# Normalize only specified columns
# Seed being used: #> Normalize --columns High Low --minMax 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 

#> Visualize 

#> Normalize --columns High Low --minMax 

#> Visualize 



# Example 3
# Normalize specified columns with a where condition
# Seed being used: #> Normalize --columns Open  --minMax --where _High_ > 100 
# ******************************************************
# ******************************************************


# Reset original dataframe
#> Data AppleStock.csv 

#> Visualize 

#> Normalize --columns Open  --minMax --where _High_ > 100 

#> Visualize 





