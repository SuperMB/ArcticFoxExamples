
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Sort the rows on a column with default sorting
# Seed being used: #> RowSort --columns High 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowSort --columns High 

#> Visualize 



# Example 2
# Sort the rows on a column and specify the order
# Seed being used: #> RowSort --columns Volume --order descending 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data AppleStock.csv 

#> Visualize 

#> RowSort --columns Volume --order descending 

#> Visualize 



# Example 3
# Sort the rows on multiple columns and specify the order
# and one column is specified by column number, not name
# Seed being used: #> RowSort --columns High 4 --order descending ascending 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data AppleStock.csv 

#> Visualize 

#> RowSort --columns High 4 --order descending ascending 

#> Visualize 


