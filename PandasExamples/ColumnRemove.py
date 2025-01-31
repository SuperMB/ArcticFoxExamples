
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

# Example 1: Column Remove with multiple columns
#> ColumnRemove  TransactionID TransactionDuration --print 
bankTransactionsDf.drop(columns= ['TransactionID', 'TransactionDuration'] , inplace=True)
print(bankTransactionsDf) #)1 
bankTransactionsDf.drop(columns= ['TransactionID', 'TransactionDuration'] , inplace=True)
print(bankTransactionsDf) #)1
bankTransactionsDf.drop(columns= ['TransactionID', 'TransactionDuration'] , inplace=True)
print(bankTransactionsDf) ##1

# Example 2: Column Remove with single columns
#> ColumnRemove CustomerAge --print 
bankTransactionsDf.drop(columns='CustomerAge', inplace=True)
print(bankTransactionsDf) #)2 
bankTransactionsDf.drop(columns='CustomerAge', inplace=True)
print(bankTransactionsDf) #)2
bankTransactionsDf.drop(columns='CustomerAge', inplace=True)
print(bankTransactionsDf) ##2
