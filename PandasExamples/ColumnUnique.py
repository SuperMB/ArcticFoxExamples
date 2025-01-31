
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data bankTransactions.csv 
bankTransactionsDf = pd.read_csv('bankTransactions.csv')
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



# Example
# Unique column with single columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

#> ColumnUnique CustomerAge --print 
bankTransactionsDfUnique = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique) #)2 



# Example
# Unique column with multiple columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 

#> ColumnUnique AccountBalance CustomerAge --print 
bankTransactionsDfUnique_1_AccountBalance = bankTransactionsDf['AccountBalance'].unique()
bankTransactionsDfUnique_1_CustomerAge = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique_1CustomerAge) #)4 
