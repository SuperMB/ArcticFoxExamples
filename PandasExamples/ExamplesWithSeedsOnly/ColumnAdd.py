
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

# Get some of the columns from the data frame
#> ColumnGet --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 

# Then, remove those columns
#> ColumnRemove --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 



# Example 1
# Add new empty column
# Seed being used: #> ColumnAdd --newColumnNames NewEmptyColumn 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnAdd --newColumnNames NewEmptyColumn 

#> Visualize 



# Example 2
# Add a column with a default value
# Seed being used: #> ColumnAdd 1 --newColumnNames Columnof1s 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnAdd 1 --newColumnNames Columnof1s 

#> Visualize 



# Example 3
# Add location, which is a series previously extracted, as a new column
# Seed being used: #> ColumnAdd location 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnAdd location 

#> Visualize 


