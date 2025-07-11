 
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
# Describe all column in the dataframe
# Seed being used: #> DataframeDescribe --print 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
#> DataframeDescribe --print --example 
bankTransactionsDfDescribe = bankTransactionsDf.describe()
print(bankTransactionsDfDescribe) #)2 
##***        TransactionAmount                TransactionDate  CustomerAge  TransactionDuration  LoginAttempts  AccountBalance        PreviousTransactionDate
##*** count        2512.000000                           2512  2512.000000          2512.000000    2512.000000     2512.000000                           2512
##*** mean          297.593778  2023-07-05 20:32:10.826433024    44.673965           119.643312       1.124602     5114.302966  2024-11-04 08:09:22.219745024
##*** min             0.260000            2023-01-02 16:00:06    18.000000            10.000000       1.000000      101.250000            2024-11-04 08:06:23
##*** 25%            81.885000  2023-04-03 16:22:05.750000128    27.000000            63.000000       1.000000     1504.370000            2024-11-04 08:07:53
##*** 50%           211.140000     2023-07-07 17:49:43.500000    45.000000           112.500000       1.000000     4735.510000            2024-11-04 08:09:22
##*** 75%           414.527500     2023-10-06 18:40:53.500000    59.000000           161.000000       1.000000     7678.820000  2024-11-04 08:10:53.249999872
##*** max          1919.110000            2024-01-01 18:21:50    80.000000           300.000000       5.000000    14977.990000            2024-11-04 08:12:23
##*** std           291.946243                            NaN    17.792198            69.963757       0.602662     3900.942499                            NaN



# Example 2
# Describe only specified columns in the dataframe
# Seed being used: #> DataframeDescribe TransactionAmount TransactionDate AccountBalance --print 
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

#> DataframeDescribe TransactionAmount TransactionDate AccountBalance --print --example 
bankTransactionsDfDescribe = bankTransactionsDf [ ['TransactionAmount', 'TransactionDate', 'AccountBalance'] ].describe()
print(bankTransactionsDfDescribe) #)4 
##***        TransactionAmount                TransactionDate  AccountBalance
##*** count        2512.000000                           2512     2512.000000
##*** mean          297.593778  2023-07-05 20:32:10.826433024     5114.302966
##*** min             0.260000            2023-01-02 16:00:06      101.250000
##*** 25%            81.885000  2023-04-03 16:22:05.750000128     1504.370000
##*** 50%           211.140000     2023-07-07 17:49:43.500000     4735.510000
##*** 75%           414.527500     2023-10-06 18:40:53.500000     7678.820000
##*** max          1919.110000            2024-01-01 18:21:50    14977.990000
##*** std           291.946243                            NaN     3900.942499


