
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



# Example
# Round with single column
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

#> ColumnRound AccountBalance 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance']) 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)2 



# Example
# Round with multiple columns
# Seed being used: #>
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 

#> ColumnRound AccountBalance TransactionAmount 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount']) 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)4 

