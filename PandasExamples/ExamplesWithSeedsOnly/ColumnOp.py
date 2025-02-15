
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Column Op where AccountBalance is multiplied with 10 for all customers above age 35
# Seed being used: #> ColumnOp _AccountBalance_ * 10 --where _CustomerAge_ > 35 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnOp _AccountBalance_ * 10 --where _CustomerAge_ > 35 

#> Visualize --count 15 



# Example 2
# Column Op where LoginAttempts is set to 6 for all customers below age 20
# Seed being used: #> ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 

#> Visualize --count 15 



