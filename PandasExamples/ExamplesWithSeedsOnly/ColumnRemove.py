
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Remove a single column by column name
# Seed being used: #> ColumnRemove CustomerAge 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRemove CustomerAge 

#> Visualize 


# Example 2
# Remove multiple columns
# Seed being used: #> ColumnRemove TransactionID TransactionDuration 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRemove TransactionID TransactionDuration 

#> Visualize 



# Example 3
# Remove multiple columns by a mix of name and index
# Seed being used: #> ColumnRemove TransactionType 2 3 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRemove TransactionType 2 3 

#> Visualize 



# Example 4
# Remove all non-numeric columns
# Seed being used: #> ColumnRemove --nonNumeric 
# ******************************************************
# ******************************************************

# Reset to the original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRemove --nonNumeric 

#> Visualize 



