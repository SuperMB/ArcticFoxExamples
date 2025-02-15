
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data banktransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Calculate column max of a single column
# Seed being used: #> ColumnMax TransactionAmount 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMax TransactionAmount 

#> print 



# Example 2
# Calculate column max of multiple columns
# Seed being used: #> ColumnMax CustomerAge AccountBalance TransactionDate 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMax CustomerAge AccountBalance TransactionDate 

#> print 



# Example 3
# Calculate column max of a column on a sliding window of the last 5 transactions, and
# add the result back into the dataframe as a new column
# Seed being used: #> ColumnMax --columns TransactionAmount --rolling 5 --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnMax --columns TransactionAmount --rolling 5 --addToDataframe 

#> Visualize --count 15 


