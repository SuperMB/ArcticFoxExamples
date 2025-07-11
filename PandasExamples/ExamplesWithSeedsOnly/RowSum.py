
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data TexasCensusCleaned.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Sum 3 rows together and have the result added to the dataframe
# after the last summed row
#
# Seed being used: #> RowSum 2 3 4 
# ******************************************************
# ******************************************************

#> Visualize --count 10 

#> RowSum 2 3 4 

#> Visualize --count 10 



# Example 2
# Sum 2 rows together, have the result added to the dataframe,
# and remove the oringal rows
#
# Seed being used: #> RowSum 2 3 --replace 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data TexasCensusCleaned.csv 

#> Visualize --count 10 

#> RowSum 2 3 --replace 

#> Visualize --count 10 


# Example 3
# Sum 3 rows together, have the result added to the dataframe,
# remove the oringal rows, and specify a value a column of
# the summed row
#
# Seed being used: #> RowSum 2 3 4 --replace --columns 0 --newValues Young  People 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data TexasCensusCleaned.csv 

#> Visualize --count 10 

#> RowSum 2 3 4 --replace --columns 0 --newValues Young  People 

#> Visualize --count 10 



# Example 4
# Sum 2 rows together within a for loop
#
# Seed being used: #> RowSum row1 row2 --replace --columns 0 --newValues category 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data TexasCensusCleaned.csv 

#> Visualize --count 10 

for i in range(9):
    row1 = i * 2
    row2 = row1 + 1
    category = 'Age Group ' + str(i)

    #> RowSum row1 row2 --replace --columns 0 --newValues category 

# Reset the indexes to reflect the new row order
#> ResetIndexes 

#> Visualize --count 10 




