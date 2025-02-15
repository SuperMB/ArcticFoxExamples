
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data pizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Get the total number of rows and print the result into the file
# Seed being used: #> RowCount --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowCount --print 
pizzeriasDfRowCount = pizzeriasDf.shape[0]



# Example 2
# Count the number of rows with missing values
# Seed being used: #> RowCount --missing 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowCount --missing 

#> print 



# Example 3
# Count the number of rows WITHOUT missing values
# Seed being used: #> RowCount --notMissing 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowCount --notMissing 

#> print 



# Example 4
# Count the number of rows where a specified value occurs
# Seed being used: #> RowCount --values 3.0 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowCount --values 3.0 

#> print 



# Example 5
# Count the number of rows that meet a criteria
# Seed being used: #> RowCount --where _Specialty  Pizza_ == Hawaiian and _Rating_ < 3.5 
# ******************************************************
# ******************************************************

#> Visualize 

#> RowCount --where _Specialty  Pizza_ == Hawaiian and _Rating_ < 3.5 

#> print 




