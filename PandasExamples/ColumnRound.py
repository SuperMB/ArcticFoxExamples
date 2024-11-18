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

# Example 1: Round with multiple columns
#⮞ ColumnRound AccountBalance TransactionAmount --print ⮜#@>4
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount'])
print(bankTransactionsDf) ##1#<4

# Example 2: Round with single column
#⮞ ColumnRound AccountBalance ⮜#@>5
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])#<5
