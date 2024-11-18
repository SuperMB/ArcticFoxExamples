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

# Example 1: Column Quantile with single column
#⮞ ColumnQuantile CustomerAge --print ⮜#@>4
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile()
print(bankTransactionsDfQuantile) ##1#<4

# Example 2: Column Quantile with multiple columns
#⮞ ColumnQuantile AccountBalance TransactionDuration --print ⮜#@>5
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDuration'] ].quantile()
print(bankTransactionsDfQuantile) ##2#<5
