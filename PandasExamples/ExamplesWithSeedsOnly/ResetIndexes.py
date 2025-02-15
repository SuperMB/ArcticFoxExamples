
#> DontProcessFile  
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Remove rows from the dataframe, then the indexes will not
# be sequential. Use ResetIndexes seed to reset the indexes.
# ResetIndexes does not take any options.
#
# Seed being used: #> ResetIndexes 
# ******************************************************
# ******************************************************

#> Visualize --count 10 

bankTransactionsDf = bankTransactionsDf.drop(bankTransactionsDf.index[3:9])

#> Visualize --count 10 

#> ResetIndexes 

#> Visualize --count 10 


