
import pandas as pd
import numpy as np

#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate'])
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')

#> ColumnHeaders 
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
# PreviousTransactionDate 
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
# PreviousTransactionDate
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
# PreviousTransactionDate

# Example 1: column sum with single columns
#> ColumnSum  AccountBalance --print 
bankTransactionsDfSum = bankTransactionsDf['AccountBalance'].sum()
print(bankTransactionsDfSum) #)1 
bankTransactionsDfSum = bankTransactionsDf['AccountBalance'].sum()
print(bankTransactionsDfSum) #)1
bankTransactionsDfSum = bankTransactionsDf['AccountBalance'].sum()
print(bankTransactionsDfSum) ##1

# Example 2: column sum with multiple columns
#> ColumnSum TransactionAmount AccountBalance --print 
bankTransactionsDfSum = bankTransactionsDf [ ['TransactionAmount', 'AccountBalance'] ].sum()
print(bankTransactionsDfSum) #)2 
bankTransactionsDfSum = bankTransactionsDf [ ['TransactionAmount', 'AccountBalance'] ].sum()
print(bankTransactionsDfSum) #)2
bankTransactionsDfSum = bankTransactionsDf [ ['TransactionAmount', 'AccountBalance'] ].sum()
print(bankTransactionsDfSum) ##2
