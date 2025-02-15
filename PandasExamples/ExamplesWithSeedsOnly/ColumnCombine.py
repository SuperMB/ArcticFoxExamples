
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data ModifiedPizzerias.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# ColumnCombine is a bit of a niche seed. The resulting code will
# combine two columns by keeping the value of the first column if
# it is not null / NaN, and if it is, the column will take the
# value of the second column.
#
# In this example, we have two people's ratings in the columns
# First Person Rating and Second Person Rating. However, each
# person did not rate every pizzeria. We will combine the two
# columns to use the First Person Rating when available, and
# otherwise use the Second Person Rating.
#
# Seed being used: #> ColumnCombine First  Person  Rating Second  Person  Rating --keepNonNull 
# ******************************************************
# ******************************************************

#> Visualize --count 20 

#> ColumnCombine First  Person  Rating Second  Person  Rating --keepNonNull 

#> ColumnRename --columns First  Person  Rating --to Total  Rating 

#> Visualize --count 20 


