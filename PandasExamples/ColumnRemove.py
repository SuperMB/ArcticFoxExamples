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

# Example 1: Column Remove with multiple columns
#⮞ ColumnRemove  TransactionID TransactionDuration --print ⮜#@>4
bankTransactionsDf.drop(columns= ['TransactionID', 'TransactionDuration'] , inplace=True)
print(bankTransactionsDf) ##1#<4

# Example 2: Column Remove with single columns
#⮞ ColumnRemove CustomerAge --print ⮜#@>5
bankTransactionsDf.drop(columns='CustomerAge', inplace=True)
print(bankTransactionsDf) ##2#<5
