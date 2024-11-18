#>1
import pandas as pd
import numpy as np#<1

#⮞ Data BankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<2

#⮞ ColumnHeaders  ⮜#@>3
# TransactionID
# AccountID
# TransactionAmount
# TransactionDate
# TransactionType
# Location
# DeviceID
# IP Address
# MerchantID
# Channel
# CustomerAge
# CustomerOccupation
# TransactionDuration
# LoginAttempts
# AccountBalance
# PreviousTransactionDate#<3

# Example 1: Column Rename with multiple columns
#⮞ ColumnRename TransactionID AccountID --to tid aid --print ⮜#@>4
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionID': 'tid', 'AccountID': 'aid'})
print(bankTransactionsDf) ##1#<4

# Example 2: Column Rename with single columns
#⮞ ColumnRename CustomerAge --to Age --print ⮜#@>5
bankTransactionsDf = bankTransactionsDf.rename(columns={'CustomerAge': 'Age'})
print(bankTransactionsDf) ##2#<5
