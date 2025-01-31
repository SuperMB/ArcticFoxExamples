
import pandas as pd
import numpy as np

#> Data banktransactions.csv 
banktransactionsDf = pd.read_csv('banktransactions.csv')
banktransactionsDf['TransactionDate'] = pd.to_datetime(banktransactionsDf['TransactionDate'])
banktransactionsDf['PreviousTransactionDate'] = pd.to_datetime(banktransactionsDf['PreviousTransactionDate']) 
banktransactionsDf = pd.read_csv('../banktransactions.csv')

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

# Example 1: Calculates Column max with single column
#> ColumnMax TransactionAmount 
banktransactionsDfMax = banktransactionsDf['TransactionAmount'].max() 
banktransactionsDfMax = banktransactionsDf['TransactionAmount'].max()

# Example 1: Calculates Column Max of multiple columns
#> ColumnMax TransactionAmount AccountBalance TransactionDate 
banktransactionsDfMax = banktransactionsDf [ ['TransactionAmount', 'AccountBalance', 'TransactionDate'] ].max() 
banktransactionsDfMax = banktransactionsDf [ ['TransactionAmount', 'AccountBalance', 'TransactionDate'] ].max()

#> print 
print(banktransactionsDfMax) #)1 
print(banktransactionsDfMax) ##1
