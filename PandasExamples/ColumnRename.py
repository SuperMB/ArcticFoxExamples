
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

# Example 1: Column Rename with multiple columns
#> ColumnRename TransactionID AccountID --to tid aid --print 
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionID': 'tid', 'AccountID': 'aid'})
print(bankTransactionsDf) #)1 
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionID': 'tid', 'AccountID': 'aid'})
print(bankTransactionsDf) #)1
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionID': 'tid', 'AccountID': 'aid'})
print(bankTransactionsDf) ##1

# Example 2: Column Rename with single columns
#> ColumnRename CustomerAge --to Age --print 
bankTransactionsDf = bankTransactionsDf.rename(columns={'CustomerAge': 'Age'})
print(bankTransactionsDf) #)2 
bankTransactionsDf = bankTransactionsDf.rename(columns={'CustomerAge': 'Age'})
print(bankTransactionsDf) #)2
bankTransactionsDf = bankTransactionsDf.rename(columns={'CustomerAge': 'Age'})
print(bankTransactionsDf) ##2
