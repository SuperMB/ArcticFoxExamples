#>1
import pandas as pd
import numpy as np#<1

#⮞ Data pizzerias.csv ⮜#@>2
pizzeriasDf = pd.read_csv('../pizzerias.csv')#<2

#⮞ ColumnHeaders  ⮜#@>3
# Pizzeria Name
# Location
# Specialty Pizza
# Price Range
# Rating
# Delivery Options
# Vegan Friendly
# Established Year
# Seating Capacity
# Website#<3

#⮞ Data  BankTransactions.csv ⮜#@>4
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<4

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
