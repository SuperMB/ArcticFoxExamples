
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# ColumnFor writes a for loop to loop through the columns
# in the dataframe. The column variable will be a string
# for each column name in the dataframe. The column variable
# can then be used in other seeds or to do column wise operations
# within the dataframe.
#
# Seed being used: #> ColumnFor 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnFor 
    if 'ID' in column:
        #> ColumnRename --columns column --replace ID --with Number 

#> Visualize 


