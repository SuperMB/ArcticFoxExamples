#>1
import pandas as pd
import numpy as np#<1


#⮞ Data BankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<2

# Example 1
# Change the values of rows 2, 4, and 5 for the column Account, changing the value to inactive
#⮞ ChangeCells --rows 2 4 5 --columns AccountID --value Inactive ⮜#@>3
bankTransactionsDf.loc[[2, 4, 5], 'AccountID' ] = 'Inactive'#<3

# Example 2
#⮞ ChangeCells  ⮜ 

# Example 3


