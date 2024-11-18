#>1
import pandas as pd
import numpy as np#<1

#⮞ Data banktransactions.csv ⮜#@>2
banktransactionsDf = pd.read_csv('../banktransactions.csv')#<2

#⮞ ColumnHeaders  ⮜#@>3
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

# Example 1: Calculates Column max with single column
#⮞ ColumnMax TransactionAmount ⮜#@>4
banktransactionsDfMax = banktransactionsDf['TransactionAmount'].max()#<4

# Example 1: Calculates Column Max of multiple columns
#⮞ ColumnMax TransactionAmount AccountBalance TransactionDate ⮜#@>5
banktransactionsDfMax = banktransactionsDf [ ['TransactionAmount', 'AccountBalance', 'TransactionDate'] ].max()#<5

#⮞ print  ⮜#@>6
print(banktransactionsDfMax) ##1#<6
