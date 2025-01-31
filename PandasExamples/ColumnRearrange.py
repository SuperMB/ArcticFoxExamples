
import pandas as pd
import numpy as np

pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 

pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)

#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')

#> ColumnRearrange 3 
columnsToMove = [bankTransactionsDf.columns[3]]
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 
columnsToMove = [bankTransactionsDf.columns[3]]
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove]

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

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 
# Code added to start of file to display all columns for dataframes

# Example 1: Column Rearrange with multiple columns, moves columns to the start
#> ColumnRearrange TransactionID MerchantID Channel 
columnsToMove = ['TransactionID', 'MerchantID', 'Channel']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 
columnsToMove = ['TransactionID', 'MerchantID', 'Channel']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove]

#> print 
print(bankTransactionsDf) #)1 
print(bankTransactionsDf) ##1
