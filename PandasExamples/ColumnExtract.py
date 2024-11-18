#>1
import pandas as pd
import numpy as np#<1

#⮞ Data BankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<2

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

#Example 1: Extarct single column
#⮞ ColumnExtract DeviceID ⮜#@>4
bankTransactionsDf = bankTransactionsDf[ [ 'DeviceID' ] ]#<4

#Example 2: Extarct multiple columns
#⮞ ColumnExtract Location AccountBalance ⮜ #⮞ `> ⮜#@>5
bankTransactionsDf = bankTransactionsDf[ [ 'Location', 'AccountBalance' ] ]#<5


#⮞ print  ⮜#@>6
print(bankTransactionsDf) ##1#<6
