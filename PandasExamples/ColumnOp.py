
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



# Example 1
# Column Op where AccountBalance is multiplied with 10 for all customers above age 35
# Seed being used: #> ColumnOp _AccountBalance_ * 10 --where _CustomerAge_ > 35 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnOp _AccountBalance_ * 10 --where _CustomerAge_ > 35 
whereCondition = bankTransactionsDf['CustomerAge'] > 35
bankTransactionsDf['AccountBalance'][whereCondition] = bankTransactionsDf['AccountBalance'] * 10 

#> Visualize --count 15 
print(bankTransactionsDf.head(n=15)) #)2 
##***    TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0       TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1        51122.10     2024-11-04 08:08:08
##*** 1       TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1       137589.10     2024-11-04 08:09:35
##*** 2       TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3       TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4       TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
##*** 5       TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1          781.68     2024-11-04 08:06:36
##*** 6       TX000007   AC00199               7.08 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1       133167.10     2024-11-04 08:10:09
##*** 7       TX000008   AC00069             171.42 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1        27962.40     2024-11-04 08:10:55
##*** 8       TX000009   AC00135             106.23 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1        90951.40     2024-11-04 08:11:14
##*** 9       TX000010   AC00385             815.96 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1        10218.80     2024-11-04 08:06:32
##*** 10      TX000011   AC00150              17.78 2023-03-14 16:46:10          Credit    Albuquerque  D000205     213.15.9.253       M073  Online           52           Engineer                   59              1        75995.20     2024-11-04 08:06:45
##*** 11      TX000012   AC00459             190.02 2023-02-06 17:30:00           Debit        Memphis  D000589   116.175.11.222       M030  Online           21            Student                  173              1         1528.81     2024-11-04 08:07:12
##*** 12      TX000013   AC00392             494.52 2023-06-07 17:21:28          Credit           Mesa  D000032   210.98.198.143       M057  Branch           24            Student                  111              1         1620.02     2024-11-04 08:08:38
##*** 13      TX000014   AC00264             781.76 2023-11-20 16:39:15           Debit        Memphis  D000054     193.83.0.183       M025     ATM           26            Student                  123              1          189.69     2024-11-04 08:07:06
##*** 14      TX000015   AC00085             166.99 2023-02-13 16:53:57           Debit     Louisville  D000309   188.124.181.12       M017  Online           18            Student                  134              1          299.93     2024-11-04 08:10:09



# Example 2
# Column Op where LoginAttempts is set to 6 for all customers below age 20
# Seed being used: #> ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1        51122.10     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1       137589.10     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnOp _LoginAttempts_ = 6 --where _CustomerAge_ < 20 
whereCondition = bankTransactionsDf['CustomerAge'] < 20
bankTransactionsDf['LoginAttempts'][whereCondition] = 6 

#> Visualize --count 15 
print(bankTransactionsDf.head(n=15)) #)4 
##***    TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0       TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1        51122.10     2024-11-04 08:08:08
##*** 1       TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1       137589.10     2024-11-04 08:09:35
##*** 2       TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              6         1122.35     2024-11-04 08:07:04
##*** 3       TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4       TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
##*** 5       TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              6          781.68     2024-11-04 08:06:36
##*** 6       TX000007   AC00199               7.08 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1       133167.10     2024-11-04 08:10:09
##*** 7       TX000008   AC00069             171.42 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1        27962.40     2024-11-04 08:10:55
##*** 8       TX000009   AC00135             106.23 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1        90951.40     2024-11-04 08:11:14
##*** 9       TX000010   AC00385             815.96 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1        10218.80     2024-11-04 08:06:32
##*** 10      TX000011   AC00150              17.78 2023-03-14 16:46:10          Credit    Albuquerque  D000205     213.15.9.253       M073  Online           52           Engineer                   59              1        75995.20     2024-11-04 08:06:45
##*** 11      TX000012   AC00459             190.02 2023-02-06 17:30:00           Debit        Memphis  D000589   116.175.11.222       M030  Online           21            Student                  173              1         1528.81     2024-11-04 08:07:12
##*** 12      TX000013   AC00392             494.52 2023-06-07 17:21:28          Credit           Mesa  D000032   210.98.198.143       M057  Branch           24            Student                  111              1         1620.02     2024-11-04 08:08:38
##*** 13      TX000014   AC00264             781.76 2023-11-20 16:39:15           Debit        Memphis  D000054     193.83.0.183       M025     ATM           26            Student                  123              1          189.69     2024-11-04 08:07:06
##*** 14      TX000015   AC00085             166.99 2023-02-13 16:53:57           Debit     Louisville  D000309   188.124.181.12       M017  Online           18            Student                  134              6          299.93     2024-11-04 08:10:09

