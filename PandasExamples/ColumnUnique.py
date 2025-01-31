
import pandas as pd
import numpy as np

#> Data bankTransactions.csv 
bankTransactionsDf = pd.read_csv('bankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 
bankTransactionsDf = pd.read_csv('../bankTransactions.csv')

# Example 1: Unique column with single columns
#> ColumnUnique CustomerAge --print 
bankTransactionsDfUnique_1 = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique_1) #)1 
bankTransactionsDfUnique = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique) ##1

# Example 2: Unique column with multiple columns
#> ColumnUnique AccountBalance CustomerAge --print 
#***Analyze bankTransactionsDfUnique to learn about: type
#***#> `run script and gather data 
bankTransactionsDfUnique_1AccountBalance = bankTransactionsDf['AccountBalance'].unique()
bankTransactionsDfUnique_1CustomerAge = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique_1CustomerAge) ##2
