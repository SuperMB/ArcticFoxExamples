
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

# Example 1: Round with multiple columns
#> ColumnRound AccountBalance TransactionAmount --print 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount'])
print(bankTransactionsDf) #)1 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount'])
print(bankTransactionsDf) #)1
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount'])
print(bankTransactionsDf) ##1

# Example 2: Round with single column
#> ColumnRound AccountBalance 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance']) 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
