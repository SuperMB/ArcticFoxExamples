
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data pizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Removing missing data from the dataframe
# Seed being used: #> CleanData --removeMissing 
# ******************************************************
# ******************************************************

#> Visualize 

#> CleanData --removeMissing 

#> Visualize 


# Example 2
# Fill missing Rating values with mean of the column
# Seed being used: #> CleanData --fill --columns Rating --mean 
# ******************************************************
# ******************************************************

# Reload the data since the last example removed the missing value
#> Data pizzerias.csv 

#> Visualize 

#> CleanData --fill --columns Rating --mean 

#> Visualize 



# Example 3
# Interpolate missing Rating values using the nearest non-NaN values
# Seed being used: #> CleanData --interpolate --columns Rating 
# ******************************************************
# ******************************************************

# Reload the data since the last example filled in missing values with the mean
#> Data pizzerias.csv 

#> Visualize 

#> CleanData --interpolate --columns Rating 

#> Visualize 


