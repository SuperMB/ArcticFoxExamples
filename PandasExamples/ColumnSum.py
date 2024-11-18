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

# Example 1: column sum with single columns
#⮞ ColumnSum  AccountBalance --print ⮜#@>4
bankTransactionsDfSum = bankTransactionsDf['AccountBalance'].sum()
print(bankTransactionsDfSum) ##1#<4

# Example 2: column sum with multiple columns
#⮞ ColumnSum TransactionAmount AccountBalance --print ⮜#@>5
bankTransactionsDfSum = bankTransactionsDf [ ['TransactionAmount', 'AccountBalance'] ].sum()
print(bankTransactionsDfSum) ##2#<5
