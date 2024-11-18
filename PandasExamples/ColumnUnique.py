#>1
import pandas as pd
import numpy as np#<1

#⮞ Data bankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../bankTransactions.csv')#<2

# Example 1: Unique column with single columns
#⮞ ColumnUnique CustomerAge --print ⮜#@>3
bankTransactionsDfUnique = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique) ##1#<3

# Example 2: Unique column with multiple columns
#⮞ ColumnUnique AccountBalance CustomerAge --print ⮜#@>4
bankTransactionsDfUnique_1AccountBalance = bankTransactionsDf['AccountBalance'].unique()
bankTransactionsDfUnique_1CustomerAge = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique_1CustomerAge) ##2#<4
