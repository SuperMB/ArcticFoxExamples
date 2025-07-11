 
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
# Round all columns to the nearest integer number
# Seed being used: #> ColumnRound 
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

#> ColumnRound --example 
for column in bankTransactionsDf.select_dtypes(include=['number']).columns:
    bankTransactionsDf[column] = round(bankTransactionsDf[column]) 


#> Visualize 
print(bankTransactionsDf.head()) #)2 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128               14.0 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1          5112.0     2024-11-04 08:08:08
##*** 1      TX000002   AC00455              376.0 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1         13759.0     2024-11-04 08:09:35
##*** 2      TX000003   AC00019              126.0 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1          1122.0     2024-11-04 08:07:04
##*** 3      TX000004   AC00070              184.0 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1          8569.0     2024-11-04 08:09:06
##*** 4      TX000005   AC00411               13.0 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1          7429.0     2024-11-04 08:06:39



# Example 2
# Round to the nearest number for a single column
# Seed being used: #> ColumnRound AccountBalance 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRound AccountBalance --example 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance']) 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)4 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1          5112.0     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1         13759.0     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              1          1122.0     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1          8569.0     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1          7429.0     2024-11-04 08:06:39
##*** 5      TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1           782.0     2024-11-04 08:06:36
##*** 6      TX000007   AC00199               7.08 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1         13317.0     2024-11-04 08:10:09
##*** 7      TX000008   AC00069             171.42 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1          2796.0     2024-11-04 08:10:55
##*** 8      TX000009   AC00135             106.23 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1          9095.0     2024-11-04 08:11:14
##*** 9      TX000010   AC00385             815.96 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1          1022.0     2024-11-04 08:06:32



# Example 3
# Round to the nearest number for multiple columns
# Seed being used: #> ColumnRound AccountBalance TransactionAmount 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRound AccountBalance TransactionAmount --example 
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'])
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount']) 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)6 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128               14.0 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1          5112.0     2024-11-04 08:08:08
##*** 1      TX000002   AC00455              376.0 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1         13759.0     2024-11-04 08:09:35
##*** 2      TX000003   AC00019              126.0 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              1          1122.0     2024-11-04 08:07:04
##*** 3      TX000004   AC00070              184.0 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1          8569.0     2024-11-04 08:09:06
##*** 4      TX000005   AC00411               13.0 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1          7429.0     2024-11-04 08:06:39
##*** 5      TX000006   AC00393               92.0 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1           782.0     2024-11-04 08:06:36
##*** 6      TX000007   AC00199                7.0 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1         13317.0     2024-11-04 08:10:09
##*** 7      TX000008   AC00069              171.0 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1          2796.0     2024-11-04 08:10:55
##*** 8      TX000009   AC00135              106.0 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1          9095.0     2024-11-04 08:11:14
##*** 9      TX000010   AC00385              816.0 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1          1022.0     2024-11-04 08:06:32



# Example 4
# Round to the nearest multiple of a number for multiple columns
# Seed being used: #> ColumnRound --columns TransactionAmount AccountBalance --to 5.5 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)7 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRound --columns TransactionAmount AccountBalance --to 5.5 --example 
bankTransactionsDf['TransactionAmount'] = round(bankTransactionsDf['TransactionAmount'] / 5.5) * 5.5
bankTransactionsDf['AccountBalance'] = round(bankTransactionsDf['AccountBalance'] / 5.5) * 5.5 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)8 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128               16.5 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1          5109.5     2024-11-04 08:08:08
##*** 1      TX000002   AC00455              374.0 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  141              1         13761.0     2024-11-04 08:09:35
##*** 2      TX000003   AC00019              126.5 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   56              1          1122.0     2024-11-04 08:07:04
##*** 3      TX000004   AC00070              187.0 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   25              1          8569.0     2024-11-04 08:09:06
##*** 4      TX000005   AC00411               11.0 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1          7430.5     2024-11-04 08:06:39
##*** 5      TX000006   AC00393               93.5 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1           781.0     2024-11-04 08:06:36
##*** 6      TX000007   AC00199                5.5 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1         13315.5     2024-11-04 08:10:09
##*** 7      TX000008   AC00069              170.5 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  291              1          2794.0     2024-11-04 08:10:55
##*** 8      TX000009   AC00135              104.5 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   86              1          9097.0     2024-11-04 08:11:14
##*** 9      TX000010   AC00385              814.0 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1          1023.0     2024-11-04 08:06:32



# Example 5
# Round to the nearest multiple of a number for multiple columns
# while only applying to rows that meet a specified criteria
# Seed being used: #> ColumnRound --columns TransactionAmount TransactionDuration --to 10 --where _TransactionAmount_ > 100 
# ******************************************************
# ******************************************************

# Reset to original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)9 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRound --columns TransactionAmount TransactionDuration --to 10 --where _TransactionAmount_ > 100 --example 
bankTransactionsDf['TransactionAmount'][bankTransactionsDf['TransactionAmount'] > 100] = round(bankTransactionsDf['TransactionAmount'] / 10) * 10
bankTransactionsDf['TransactionDuration'][bankTransactionsDf['TransactionAmount'] > 100] = round(bankTransactionsDf['TransactionDuration'] / 10) * 10 

#> Visualize --count 10 
print(bankTransactionsDf.head(n=10)) #)10 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380   162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             380.00 2023-06-27 16:44:19           Debit        Houston  D000051      13.149.61.4       M052     ATM           68             Doctor                  140              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             130.00 2023-07-10 18:16:08           Debit           Mesa  D000235   215.97.143.157       M009  Online           19            Student                   60              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             180.00 2023-05-05 16:32:11           Debit        Raleigh  D000187   200.13.225.150       M002  Online           26            Student                   20              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308     65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
##*** 5      TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579   117.67.192.211       M054     ATM           18            Student                  172              1          781.68     2024-11-04 08:06:36
##*** 6      TX000007   AC00199               7.08 2023-02-15 16:36:48          Credit        Seattle  D000241  140.212.253.222       M019     ATM           37             Doctor                  139              1        13316.71     2024-11-04 08:10:09
##*** 7      TX000008   AC00069             170.00 2023-05-08 17:47:59          Credit   Indianapolis  D000500    92.214.76.157       M020  Branch           67            Retired                  290              1         2796.24     2024-11-04 08:10:55
##*** 8      TX000009   AC00135             110.00 2023-03-21 16:59:46          Credit        Detroit  D000690    24.148.92.177       M035  Branch           51           Engineer                   90              1         9095.14     2024-11-04 08:11:14
##*** 9      TX000010   AC00385             820.00 2023-03-31 16:06:57           Debit      Nashville  D000199     32.169.88.41       M007     ATM           55             Doctor                  120              1         1021.88     2024-11-04 08:06:32



