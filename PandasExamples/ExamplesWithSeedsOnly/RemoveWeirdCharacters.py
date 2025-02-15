
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data TexasCensus.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Remove non-standard character from the entire dataframe.
# Sometimes these are introduced accidentally or intentionally in a datset
# Seed being used: #> RemoveWeirdCharacters 
# ******************************************************
# ******************************************************

#> Visualize 

#> RemoveWeirdCharacters 

#> Visualize 



# Example 2
# Remove non-standard character from specified columns.
# Sometimes these are introduced accidentally or intentionally in a datset
# Seed being used: #> RemoveWeirdCharacters Label  (Grouping) Texas  Total  Margin  of  Error 
# ******************************************************

# Reset the dataframe
#> Data TexasCensus.csv 

#> ColumnRename --replace !! --with ' ' 

#> Visualize 

#> RemoveWeirdCharacters Label  (Grouping) Texas  Total  Margin  of  Error 

#> Visualize 



