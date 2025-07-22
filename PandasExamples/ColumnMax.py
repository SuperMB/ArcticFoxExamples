 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 




# Setup
# ******************************************************
# ******************************************************

#> Data banktransactions.csv 
banktransactionsDf = pd.read_csv('banktransactions.csv')
banktransactionsDf['TransactionDate'] = pd.to_datetime(banktransactionsDf['TransactionDate'])
banktransactionsDf['PreviousTransactionDate'] = pd.to_datetime(banktransactionsDf['PreviousTransactionDate']) 


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
# Calculate column max of a single column
# Seed being used: #> ColumnMax TransactionAmount 
# ******************************************************
# ******************************************************

#> Visualize 
print(banktransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
#> ColumnMax TransactionAmount --exampleTitle Get Max of a Single Column --example The maximum value in a column helps identify unusual or extreme entries. In this example, we compute the highest recorded TransactionAmount across all transactions.
banktransactionsDfMax = banktransactionsDf['TransactionAmount'].max() 

#> print 
print(banktransactionsDfMax) #)2 
##*** 1919.11



# Example 2
# Calculate column max of multiple columns
# Seed being used: #> ColumnMax CustomerAge AccountBalance TransactionDate 
# ******************************************************
# ******************************************************

#> Visualize 
print(banktransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnMax CustomerAge AccountBalance TransactionDate --exampleTitle Get Max of Multiple Columns --example This example shows how to retrieve the maximum values across several columns at once. It helps identify the oldest customer, the largest account balance, and the most recent transaction date in the dataset.
banktransactionsDfMax = banktransactionsDf [ ['CustomerAge', 'AccountBalance', 'TransactionDate'] ].max() 

#> print 
print(banktransactionsDfMax) #)4 
##*** CustomerAge                         80
##*** AccountBalance                14977.99
##*** TransactionDate    2024-01-01 18:21:50
##*** dtype: object



# Example 3
# Calculate column max of a column on a sliding window of the last 5 transactions, and
# add the result back into the dataframe as a new column
# Seed being used: #> ColumnMax --columns TransactionAmount --rolling 5 --addToDataframe 
# ******************************************************
# ******************************************************

#> Visualize 
print(banktransactionsDf.head()) #)5 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnMax --columns TransactionAmount --rolling 5 --addToDataframe --exampleTitle Add Rolling Max to Dataframe --example A rolling maximum provides a dynamic upper bound across a defined window of rows. Here, we compute the maximum TransactionAmount across the latest 5 entries in each row and add that result as a new column in trend analysis.
banktransactionsDfMaxRolling5 = banktransactionsDf['TransactionAmount'].rolling(window=5, min_periods=1).max()
banktransactionsDf['TransactionAmountMaxRolling5'] = pd.Series()
banktransactionsDf['TransactionAmountMaxRolling5'] = banktransactionsDfMaxRolling5 

#> Visualize --count 15 
print(banktransactionsDf.head(n=15)) #)6 
##***    TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate  TransactionAmountMaxRolling5
##*** 0       TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08                         14.09
##*** 1       TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35                        376.24
##*** 2       TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04                        376.24
##*** 3       TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06                        376.24
##*** 4       TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39                        376.24
##*** 5       TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1          781.68     2024-11-04 08:06:36                        376.24
##*** 6       TX000007   AC00199               7.08 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1        13316.71     2024-11-04 08:10:09                        184.50
##*** 7       TX000008   AC00069             171.42 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1         2796.24     2024-11-04 08:10:55                        184.50
##*** 8       TX000009   AC00135             106.23 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1         9095.14     2024-11-04 08:11:14                        171.42
##*** 9       TX000010   AC00385             815.96 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1         1021.88     2024-11-04 08:06:32                        815.96
##*** 10      TX000011   AC00150              17.78 2023-03-14 16:46:10          Credit    Albuquerque  D000205     213.15.9.253       M073  Online           52           Engineer                   59              1         7599.52     2024-11-04 08:06:45                        815.96
##*** 11      TX000012   AC00459             190.02 2023-02-06 17:30:00           Debit        Memphis  D000589   116.175.11.222       M030  Online           21            Student                  173              1         1528.81     2024-11-04 08:07:12                        815.96
##*** 12      TX000013   AC00392             494.52 2023-06-07 17:21:28          Credit           Mesa  D000032   210.98.198.143       M057  Branch           24            Student                  111              1         1620.02     2024-11-04 08:08:38                        815.96
##*** 13      TX000014   AC00264             781.76 2023-11-20 16:39:15           Debit        Memphis  D000054     193.83.0.183       M025     ATM           26            Student                  123              1          189.69     2024-11-04 08:07:06                        815.96
##*** 14      TX000015   AC00085             166.99 2023-02-13 16:53:57           Debit     Louisville  D000309   188.124.181.12       M017  Online           18            Student                  134              1          299.93     2024-11-04 08:10:09                        781.76
