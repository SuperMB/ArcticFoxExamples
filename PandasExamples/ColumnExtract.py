
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

#Example 1: Extarct single column
#> ColumnExtract DeviceID 
bankTransactionsDf = bankTransactionsDf[ [ 'DeviceID' ] ] 
bankTransactionsDf = bankTransactionsDf[ [ 'DeviceID' ] ]

#Example 2: Extarct multiple columns
#> ColumnExtract Location AccountBalance  
bankTransactionsDf = bankTransactionsDf[ [ 'Location', 'AccountBalance #>', '`', '>' ] ] 
bankTransactionsDf = bankTransactionsDf[ [ 'Location', 'AccountBalance' ] ]


#> print 
print(bankTransactionsDf) #)1 
print(bankTransactionsDf) ##1
