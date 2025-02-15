

#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Get the default quantiles of a single column
# Seed being used: #> ColumnQuantile CustomerAge 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile CustomerAge 

#> print 



# Example 2
# Get the quantiles of a single column and specify what
# quantiles to get
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 

#> print 



# Example 3
# Get the quantiles of a single column, specify what quantiles
# to get, and create a variable for each
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles 

#> print bankTransactionsDfQuantile 

#> print bankTransactionsDfQuantile0 

#> print bankTransactionsDfQuantile1 

#> print bankTransactionsDfQuantile2 

#> print bankTransactionsDfQuantile3 



# Example 4
# Get the default quantile of multiple columns
# Seed being used: #> ColumnQuantile AccountBalance TransactionDuration 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile AccountBalance TransactionDuration 

#> print 



# Example 5
# Get the quantiles of a multiple columns and specify what
# quantiles to get
# Seed being used: #> ColumnQuantile --columns AccountBalance TransactionDate --quantile .2 .4 .6 .8 1 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile --columns AccountBalance TransactionDate --quantile .2 .4 .6 .8 1 

#> print 



# Example 6
# Get the quantiles of a single column, specify what quantiles
# to get, and create a variable for each
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnQuantile --columns AccountBalance TransactionDuration --quantile .3 .6 .9 --variablesForQuantiles 


