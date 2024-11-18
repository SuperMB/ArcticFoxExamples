#>1
import pandas as pd
import numpy as np
#<1 #>2
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)#<2

#⮞ Data BankTransactions.csv ⮜#@>3
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<3

#⮞ ColumnRearrange 3 ⮜#@>4
columnsToMove = [bankTransactionsDf.columns[3]]
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove]#<4

#⮞ ColumnHeaders  ⮜#@>5
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
# PreviousTransactionDate#<5

#⮞ VisualizeAllColumns  ⮜#@>6
# Code added to start of file to display all columns for dataframes#<6

# Example 1: Column Rearrange with multiple columns, moves columns to the start
#⮞ ColumnRearrange TransactionID MerchantID Channel ⮜#@>7
columnsToMove = ['TransactionID', 'MerchantID', 'Channel']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove]#<7

#⮞ print  ⮜#@>8
print(bankTransactionsDf) ##1#<8
