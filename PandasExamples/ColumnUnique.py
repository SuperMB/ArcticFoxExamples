 
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
# Get the unique values of a single column,
# print the result to the file
# Seed being used: #> ColumnUnique CustomerAge --print 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnUnique CustomerAge --print --example 
bankTransactionsDfUnique = bankTransactionsDf['CustomerAge'].unique()
print(bankTransactionsDfUnique) #)2 
##*** [70 68 19 26 18 37 67 51 55 52 21 24 36 39 59 71 38 22 65 23 44 27 29 49
##***  45 75 66 63 57 74 41 69 28 62 25 48 46 79 56 50 42 60 32 35 20 58 34 54
##***  64 53 30 78 40 47 43 33 80 77 61 31 76 73 72]



# Example 2
# Get the unique values of multiple column
# Seed being used: #> ColumnUnique TransactionType Location 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnUnique TransactionType Location --example 
bankTransactionsDfUnique_1_TransactionType = bankTransactionsDf['TransactionType'].unique()
bankTransactionsDfUnique_1_Location = bankTransactionsDf['Location'].unique() 

#> print bankTransactionsDfUnique_1_TransactionType 
print(bankTransactionsDfUnique_1_TransactionType) #)4 
##*** ['Debit' 'Credit']

#> print bankTransactionsDfUnique_1_Location 
print(bankTransactionsDfUnique_1_Location) #)5 
##*** ['San Diego' 'Houston' 'Mesa' 'Raleigh' 'Atlanta' 'Oklahoma City'
##***  'Seattle' 'Indianapolis' 'Detroit' 'Nashville' 'Albuquerque' 'Memphis'
##***  'Louisville' 'Denver' 'Austin' 'Columbus' 'Los Angeles' 'Las Vegas'
##***  'Fort Worth' 'Miami' 'Milwaukee' 'Baltimore' 'New York' 'San Francisco'
##***  'San Jose' 'San Antonio' 'Philadelphia' 'Charlotte' 'Tucson' 'Chicago'
##***  'Sacramento' 'Kansas City' 'Omaha' 'Virginia Beach' 'Dallas' 'Boston'
##***  'Jacksonville' 'Phoenix' 'Washington' 'El Paso' 'Colorado Springs'
##***  'Fresno' 'Portland']



# Example 3
# Get the number of unique values for each column
# in the dataframe, print the result to file
# Seed being used: #> ColumnUnique TransactionType Location 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)6 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnUnique --print --example 
bankTransactionsDfUnique_1 = bankTransactionsDf.nunique()
print(bankTransactionsDfUnique_1) #)7 
##*** TransactionID              2512
##*** AccountID                   495
##*** TransactionAmount          2455
##*** TransactionDate            2512
##*** TransactionType               2
##*** Location                     43
##*** DeviceID                    681
##*** IP Address                  592
##*** MerchantID                  100
##*** Channel                       3
##*** CustomerAge                  63
##*** CustomerOccupation            4
##*** TransactionDuration         288
##*** LoginAttempts                 5
##*** AccountBalance             2510
##*** PreviousTransactionDate     360
##*** dtype: int64



