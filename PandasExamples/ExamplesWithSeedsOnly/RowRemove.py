
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data pizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Remove rows with missing values from any column
# Seed being used: #> RowRemove --missing 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowRemove --missing 

#> Visualize 



# Example 2
# Remove rows with missing values in specified columns
# Seed being used: #> RowRemove --missing --columns Rating Established  Year 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize 

#> RowRemove --missing --columns Rating Established  Year 

#> Visualize --count 10 



# Example 3
# Remove rows at an index
# Seed being used: #> RowRemove --index 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize 

#> RowRemove --index 3 

#> Visualize 



# Example 4
# Remove rows after an index
# Seed being used: #> RowRemove --indexStart 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize 

#> RowRemove --indexStart 3 

#> Visualize --count 10 



# Example 5
# Remove rows before an index
# Seed being used: #> RowRemove --indexStop 50 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize 

#> RowRemove --indexStop 50 

#> Visualize 



# Example 6
# Remove rows within a range
# Seed being used: #> RowRemove --indexStart 5 --indexStop 10 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize 

#> RowRemove --indexStart 5 --indexStop 10 

#> Visualize --count 10 



# Example 7
# Remove rows that meet a criteria
# Seed being used: #> RowRemove --where _Pizzeria  Name_ contains Antonio 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 

#> Visualize --count 10 

#> RowRemove --where _Pizzeria  Name_ contains Antonio 

#> Visualize --count 10 

