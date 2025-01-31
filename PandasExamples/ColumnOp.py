
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

# Example 1: Column Op where AccountBalance is multiplied with 10 for all customers above age 35
#> ColumnOp _AccountBalance_ *= 10 --where _CustomerAge_ > 35 --print 
whereCondition_1 = bankTransactionsDf['CustomerAge'] > 35
bankTransactionsDf['AccountBalance'] *[whereCondition_1]= 10
print(bankTransactionsDf) #)1 
whereCondition = bankTransactionsDf['CustomerAge'] > 35
bankTransactionsDf['AccountBalance'] *= 10
print(bankTransactionsDf) ##1

# Example 2: Column Op where LoginAttempts is set to 6 for all customers below age 20
#> ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 --print 
#***Analyze whereCondition to learn about: type
#***#> `run script and gather data 
whereCondition = bankTransactionsDf['CustomerAge'] < 20
bankTransactionsDf['LoginAttempts'] = 6
print(bankTransactionsDf) ##2
