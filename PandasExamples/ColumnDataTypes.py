
import pandas as pd
import numpy as np


#> Data bankTransactions.csv 
bankTransactionsDf = pd.read_csv('bankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 
bankTransactionsDf = pd.read_csv('../bankTransactions.csv')

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

# Example 1: print data types of various columns
#> ColumnDataTypes AccountID LoginAttempts TransactionAmount 
bankTransactionsDfDataTypes = bankTransactionsDf[ [ 'AccountID', 'LoginAttempts', 'TransactionAmount' ] ].dtypes 
bankTransactionsDfDataTypes = bankTransactionsDf[ [ 'AccountID', 'LoginAttempts', 'TransactionAmount' ] ].dtypes

#> print 
print(bankTransactionsDfDataTypes) #)1 
print(bankTransactionsDfDataTypes) ##1
