
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Pivoting a table to sum one column according to the categories of another column
# This pivot only uses rows, no columns for the resulting table
# Seed being used: #> DataframePivot --rows Location --cells TransactionAmount --sum 
# ******************************************************
# ******************************************************

#> Visualize 

#> DataframePivot --rows Location --cells TransactionAmount --sum 

#> print 



# Example 2
# Pivoting a table get the max of one column according to the categories of two
# other columns. This pivot uses both rows and columns for the resulting table
# Seed being used: #> DataframePivot --rows Location --columns TransactionType --cells AccountBalance --max 
# ******************************************************
# ******************************************************

# Refocus on the original dataframe
#> Focus bankTransactionsDf 

#> Visualize 

#> DataframePivot --rows Location --columns TransactionType --cells AccountBalance --max 

#> print 



# Example 3
# Pivoting a table get the count of occurences of multiple columns.
# This pivot uses both rows and columns for the resulting table, and
# uses two columns for the new columns of the pivot.
# Seed being used: #> DataframePivot --rows Location --cells TransactionAmount --sum 
# ******************************************************
# ******************************************************

# Change focus to original dataframe
#> Focus bankTransactionsDf 

#> Visualize 

#> DataframePivot --rows Location --columns Channel TransactionType --cells AccountID --count 

#> print 



# Example 4
# Pivoting a table get the sum of a column with multiple columns
# being used for both the rows and columns of the pivoted table.
# Seed being used: #> DataframePivot --rows CustomerAge TransactionType --columns Channel LoginAttempts CustomerOccupation --cells TransactionAmount --sum 
# ******************************************************
# ******************************************************

# Change focus to original dataframe
#> Focus bankTransactionsDf 

#> Visualize 

#> DataframePivot --rows CustomerAge TransactionType --columns Channel LoginAttempts CustomerOccupation --cells TransactionAmount --sum 

#> print 


