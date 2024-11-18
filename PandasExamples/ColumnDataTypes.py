#>1
import pandas as pd
import numpy as np#<1


#⮞ Data bankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../bankTransactions.csv')#<2

#⮞ ColumnHeaders ⮜#@>3
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
# PreviousTransactionDate#<3

# Example 1: print data types of various columns
#⮞ ColumnDataTypes AccountID LoginAttempts TransactionAmount ⮜#@>4
bankTransactionsDfDataTypes = bankTransactionsDf[ [ 'AccountID', 'LoginAttempts', 'TransactionAmount' ] ].dtypes#<4

#⮞ print  ⮜#@>5
print(bankTransactionsDfDataTypes) ##1#<5
