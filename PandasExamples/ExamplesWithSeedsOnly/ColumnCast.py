
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data Pizzerias.csv 

#> ColumnHeaders 

#> VisualizeAllColumns 



# NOTE
# ******************************************************
# ******************************************************
# Casting a column in pandas informs pandas on how to interpret the column,
# Casting will not work for data that does not conform to the specified cast.
# For example, you cannot cast a column of street addresses, such as:
# 138 Harp Dr.
# to and integer and expect pandas to select the numeric portion of the address.
# Instead, pandas will throw an error stating that it cannot convert the column
# to integers.
#
#
# Also, casting rows with NaN's may be an issue. If this appears, use
# RowRemow to remove rows with missing data, or CleanData to fill in missing
# data values.
# ******************************************************
# ******************************************************



# Example 1
# Casting a column to integer
# Seed being used: #> ColumnCast Rating --type int 
# ******************************************************
# ******************************************************

#> RowRemove --missing 

#> Visualize 

#> ColumnCast Rating --type int 

#> Visualize 



# Example 2
# Casting multiple columns to string
# Seed being used: #> ColumnCast Speciality  Pizza Established  Year --type string 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnCast Specialty  Pizza Established  Year --type string 

#> Visualize 



# Example 3
# Casting a column to float
# Seed being used: #> ColumnCast Seating  Capacity --type float 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnCast Seating  Capacity --type float 

#> Visualize 


