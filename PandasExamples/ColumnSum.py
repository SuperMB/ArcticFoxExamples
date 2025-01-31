
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

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



# Example 1
# column sum with single columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

#> ColumnSum  AccountBalance --print 
bankTransactionsDfSum = bankTransactionsDf['AccountBalance'].sum()
print(bankTransactionsDfSum) #)2 



# Example 2
# column sum with multiple columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 

#> ColumnSum TransactionAmount AccountBalance --print 
bankTransactionsDfSum = bankTransactionsDf [ ['TransactionAmount', 'AccountBalance'] ].sum()
print(bankTransactionsDfSum) #)4 
