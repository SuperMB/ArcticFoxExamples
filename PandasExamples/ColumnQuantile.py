
import pandas as pd
import numpy as np

#> Data BankTransactions.csv 
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

# Example 1: Column Quantile with single column
#> ColumnQuantile CustomerAge --print 
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile()
print(bankTransactionsDfQuantile) #)1 
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile()
print(bankTransactionsDfQuantile) ##1

# Example 2: Column Quantile with multiple columns
#> ColumnQuantile AccountBalance TransactionDuration --print 
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDuration'] ].quantile()
print(bankTransactionsDfQuantile) #)2 
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDuration'] ].quantile()
print(bankTransactionsDfQuantile) ##2
