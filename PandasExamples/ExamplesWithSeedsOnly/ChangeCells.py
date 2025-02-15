
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 

#> VisualizeAllColumns 



# Example 1
# Change AccountID in rows 2, 4, and 5 to Inactive
# Seed being used: #> ChangeCells --rows 2 4 5 --columns AccountID --value Inactive 
# ******************************************************
# ******************************************************

#> Visualize --count 6 

#> ChangeCells --rows 2 4 5 --columns AccountID --value Inactive 

#> Visualize --count 6 



# Example 2
# Change occurences of San Diego to Los Angeles in the Location column
# Seed being used: #> ChangeCells --initialValues San  Diego --newValues Los  Angeles --columns Location 
# ******************************************************
# ******************************************************

#> Visualize 

#> ChangeCells --initialValues San  Diego --newValues Los  Angeles --columns Location 

#> Visualize 



# Example 3
# Change transactions after June 1st 2023 to be of TransactionType cash
# This illustrates changing only cells that meet a stated criteria
# Seed being used: #> ChangeCells --columns TransactionType --value Cash --where _TransactionDate_ > 06-01-2023 --allMatchingRows 
# ******************************************************
# ******************************************************

#> Visualize 

#> ChangeCells --columns TransactionType --value Cash --where _TransactionDate_ > 06-01-2023 --allMatchingRows 

#> Visualize 
