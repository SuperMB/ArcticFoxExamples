
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Fully rename a single column by column name
# Seed being used: #> ColumnRename CustomerAge --to Age 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRename CustomerAge --to Age 

#> Visualize 


# Example 2
# Fully rename multiple columns by column name
# Seed being used: #> ColumnRename TransactionID AccountID --to tid aid 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRename TransactionID AccountID --to tid aid 

#> Visualize 



# Example 3
# Fully rename multiple columns by column name and index
# Seed being used: #> ColumnRename TransactionDate 4 5  --to Date Payment City 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRename TransactionDate 4 5  --to Date Payment City 

#> Visualize 



# Example 4
# Replace a matching piece of each column name with a new string/value
# Seed being used: #> ColumnRename --replace ID --with Identifier 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRename --replace ID --with Identifier 

#> Visualize 



# Example 5
# Replace a matching piece of specified column names and index with a new string/value
# Seed being used: #> ColumnRename --columns TransactionAmount TransactionType --replace Transaction --with Payment 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRename --columns TransactionAmount TransactionType --replace Transaction --with Payment 

#> Visualize 



