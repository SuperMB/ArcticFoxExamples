
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Specify a single column, without any other options, the
# specified column will be moved to the front of the
# dataframe
# Seed being used: #> ColumnRearrange DeviceID 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRearrange DeviceID 

#> Visualize 



# Example 2
# Specify multiple columns, without any other options, the
# multiple columns will be moved to the front of the
# dataframe
# Seed being used: #> ColumnRearrange TransactionDate MerchantID Channel 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange TransactionDate MerchantID Channel 

#> Visualize 



# Example 3
# Specify a single column by index instead of name,
# without any other options, the specified column
# will be moved to the front of the dataframe
# Seed being used: #> ColumnRearrange 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange 3 

#> Visualize 



# Example 4
# Specify multiple columns as a mix of index and name,
# without any other options, the specified columns
# will be moved to the front of the dataframe
# Seed being used: #> ColumnRearrange CustomerAge 4 5 CustomerOccupation 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange CustomerAge 4 5 CustomerOccupation 

#> Visualize 



# Example 5
# Specify a single column and the new index for the
# specified column
# Seed being used: #> ColumnRearrange --columns IP  Address --indexes 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange --columns IP  Address --indexes 3 

#> Visualize 



# Example 6
# Specify multiple columns and new indexes for each
# of the specified columns
# Seed being used: #> ColumnRearrange --columns AccountBalance LoginAttempts TransactionType --indexes 2 4 6 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange --columns AccountBalance LoginAttempts TransactionType --indexes 2 4 6 

#> Visualize 



# Example 7
# Specify multiple columns and moving those columns
# to the end of the dataframe
# Seed being used: #> ColumnRearrange TransactionID AccountID 4  --back 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRearrange TransactionID AccountID 4  --back 

#> Visualize 


