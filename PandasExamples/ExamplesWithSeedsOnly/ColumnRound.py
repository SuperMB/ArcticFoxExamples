
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Round all columns to the nearest integer number
# Seed being used: #> ColumnRound 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnRound 

#> Visualize 



# Example 2
# Round to the nearest number for a single column
# Seed being used: #> ColumnRound AccountBalance 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRound AccountBalance 

#> Visualize --count 10 



# Example 3
# Round to the nearest number for multiple columns
# Seed being used: #> ColumnRound AccountBalance TransactionAmount 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRound AccountBalance TransactionAmount 

#> Visualize --count 10 



# Example 4
# Round to the nearest multiple of a number for multiple columns
# Seed being used: #> ColumnRound --columns TransactionAmount AccountBalance --to 5.5 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRound --columns TransactionAmount AccountBalance --to 5.5 

#> Visualize --count 10 



# Example 5
# Round to the nearest multiple of a number for multiple columns
# while only applying to rows that meet a specified criteria
# Seed being used: #> ColumnRound --columns TransactionAmount TransactionDuration --to 10 --where _TransactionAmount_ > 100 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 

#> Visualize 

#> ColumnRound --columns TransactionAmount TransactionDuration --to 10 --where _TransactionAmount_ > 100 

#> Visualize --count 10 



