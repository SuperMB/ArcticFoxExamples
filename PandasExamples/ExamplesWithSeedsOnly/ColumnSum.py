
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Compute the sum of a single column, print the result to file
# Seed being used: #> ColumnSum AccountBalance --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnSum AccountBalance --print 



# Example 2
# Compute the sums of multiple columns, print the result to file
# Seed being used: #> ColumnSum TransactionAmount AccountBalance --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnSum TransactionAmount AccountBalance --print 



# Example 3
# Compute the sums of multiple columns according to a condition
# and grouped by another column, print the result to file
# Seed being used: #> ColumnSum TransactionAmount AccountBalance --print 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnSum TransactionAmount AccountBalance CustomerAge --where _TransactionAmount_ > 75 and _CustomerAge_ > 20 --group TransactionType Channel --print 



