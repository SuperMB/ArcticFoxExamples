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

# Example 1: Column Op where AccountBalance is multiplied with 10 for all customers above age 35
#⮞ ColumnOp _AccountBalance_ *= 10 --where _CustomerAge_ > 35 --print ⮜#@>4
whereCondition = bankTransactionsDf['CustomerAge'] > 35
bankTransactionsDf['AccountBalance'] *= 10
print(bankTransactionsDf) ##1#<4

# Example 2: Column Op where LoginAttempts is set to 6 for all customers below age 20
#⮞ ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 --print ⮜#@>5
whereCondition = bankTransactionsDf['CustomerAge'] < 20
bankTransactionsDf['LoginAttempts'] = 6
print(bankTransactionsDf) ##2#<5
