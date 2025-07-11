 
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
# Specify a single column, without any other options, the
# specified column will be moved to the front of the
# dataframe
# Seed being used: #> ColumnRearrange DeviceID 
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

#> ColumnRearrange DeviceID --example 
columnsToMove = ['DeviceID']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 

#> Visualize 
print(bankTransactionsDf.head()) #)2 
##***   DeviceID TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0  D000380      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1  D000051      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2  D000235      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3  D000187      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4  D000308      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 2
# Specify multiple columns, without any other options, the
# multiple columns will be moved to the front of the
# dataframe
# Seed being used: #> ColumnRearrange TransactionDate MerchantID Channel 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> ColumnRearrange TransactionDate MerchantID Channel --example 
columnsToMove = ['TransactionDate', 'MerchantID', 'Channel']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 

#> Visualize 
print(bankTransactionsDf.head()) #)4 
##***       TransactionDate MerchantID Channel TransactionID AccountID  TransactionAmount TransactionType   Location DeviceID      IP Address  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0 2023-04-11 16:29:14       M015     ATM      TX000001   AC00128              14.09           Debit  San Diego  D000380  162.198.218.92           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1 2023-06-27 16:44:19       M052     ATM      TX000002   AC00455             376.24           Debit    Houston  D000051     13.149.61.4           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2 2023-07-10 18:16:08       M009  Online      TX000003   AC00019             126.29           Debit       Mesa  D000235  215.97.143.157           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3 2023-05-05 16:32:11       M002  Online      TX000004   AC00070             184.50           Debit    Raleigh  D000187  200.13.225.150           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4 2023-10-16 17:51:24       M091  Online      TX000005   AC00411              13.45          Credit    Atlanta  D000308    65.164.3.100           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 3
# Specify a single column by index instead of name,
# without any other options, the specified column
# will be moved to the front of the dataframe
# Seed being used: #> ColumnRearrange 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> ColumnRearrange 3 --example 
columnsToMove = [bankTransactionsDf.columns[3]]
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 

#> Visualize 
print(bankTransactionsDf.head()) #)6 
##***       TransactionDate TransactionID AccountID  TransactionAmount TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0 2023-04-11 16:29:14      TX000001   AC00128              14.09           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1 2023-06-27 16:44:19      TX000002   AC00455             376.24           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2 2023-07-10 18:16:08      TX000003   AC00019             126.29           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3 2023-05-05 16:32:11      TX000004   AC00070             184.50           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4 2023-10-16 17:51:24      TX000005   AC00411              13.45          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 4
# Specify multiple columns as a mix of index and name,
# without any other options, the specified columns
# will be moved to the front of the dataframe
# Seed being used: #> ColumnRearrange CustomerAge 4 5 CustomerOccupation 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> ColumnRearrange CustomerAge 4 5 CustomerOccupation --example 
columnsToMove = ['CustomerAge', bankTransactionsDf.columns[4], bankTransactionsDf.columns[5], 'CustomerOccupation']
columnsToMove = columnsToMove + [column for column in bankTransactionsDf.columns if column not in columnsToMove]
bankTransactionsDf = bankTransactionsDf[columnsToMove] 

#> Visualize 
print(bankTransactionsDf.head()) #)8 
##***    CustomerAge TransactionType   Location CustomerOccupation TransactionID AccountID  TransactionAmount     TransactionDate DeviceID      IP Address MerchantID Channel  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0           70           Debit  San Diego             Doctor      TX000001   AC00128              14.09 2023-04-11 16:29:14  D000380  162.198.218.92       M015     ATM                   81              1         5112.21     2024-11-04 08:08:08
##*** 1           68           Debit    Houston             Doctor      TX000002   AC00455             376.24 2023-06-27 16:44:19  D000051     13.149.61.4       M052     ATM                  141              1        13758.91     2024-11-04 08:09:35
##*** 2           19           Debit       Mesa            Student      TX000003   AC00019             126.29 2023-07-10 18:16:08  D000235  215.97.143.157       M009  Online                   56              1         1122.35     2024-11-04 08:07:04
##*** 3           26           Debit    Raleigh            Student      TX000004   AC00070             184.50 2023-05-05 16:32:11  D000187  200.13.225.150       M002  Online                   25              1         8569.06     2024-11-04 08:09:06
##*** 4           26          Credit    Atlanta            Student      TX000005   AC00411              13.45 2023-10-16 17:51:24  D000308    65.164.3.100       M091  Online                  198              1         7429.40     2024-11-04 08:06:39



# Example 5
# Specify a single column and the new index for the
# specified column
# Seed being used: #> ColumnRearrange --columns IP  Address --indexes 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> ColumnRearrange --columns IP  Address --indexes 3 --example 
columnsToMove = ['IP Address']
[3] = [3]
remaining_columns = [column for column in bankTransactionsDf.columns if column not in columnsToMove]
for column,targetIndex in zip(columnsToMove, [3]):
    remaining_columns.insert(targetIndex, column)
bankTransactionsDf = bankTransactionsDf[remaining_columns] 


#> Visualize 
print(bankTransactionsDf.head()) #)10 
##***   TransactionID AccountID  TransactionAmount      IP Address     TransactionDate TransactionType   Location DeviceID MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09  162.198.218.92 2023-04-11 16:29:14           Debit  San Diego  D000380       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24     13.149.61.4 2023-06-27 16:44:19           Debit    Houston  D000051       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29  215.97.143.157 2023-07-10 18:16:08           Debit       Mesa  D000235       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50  200.13.225.150 2023-05-05 16:32:11           Debit    Raleigh  D000187       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45    65.164.3.100 2023-10-16 17:51:24          Credit    Atlanta  D000308       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 6
# Specify multiple columns and new indexes for each
# of the specified columns
# Seed being used: #> ColumnRearrange --columns AccountBalance LoginAttempts TransactionType --indexes 2 4 6 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)11 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRearrange --columns AccountBalance LoginAttempts TransactionType --indexes 2 4 6 --example 
columnsToMove = ['AccountBalance', 'LoginAttempts', 'TransactionType']
[2, 4, 6] = [2, 4, 6]
remaining_columns = [column for column in bankTransactionsDf.columns if column not in columnsToMove]
for column,targetIndex in zip(columnsToMove, [2, 4, 6]):
    remaining_columns.insert(targetIndex, column)
bankTransactionsDf = bankTransactionsDf[remaining_columns] 


#> Visualize 
print(bankTransactionsDf.head()) #)12 
##***   TransactionID AccountID  AccountBalance  TransactionAmount  LoginAttempts     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration PreviousTransactionDate
##*** 0      TX000001   AC00128         5112.21              14.09              1 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81     2024-11-04 08:08:08
##*** 1      TX000002   AC00455        13758.91             376.24              1 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141     2024-11-04 08:09:35
##*** 2      TX000003   AC00019         1122.35             126.29              1 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56     2024-11-04 08:07:04
##*** 3      TX000004   AC00070         8569.06             184.50              1 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25     2024-11-04 08:09:06
##*** 4      TX000005   AC00411         7429.40              13.45              1 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198     2024-11-04 08:06:39



# Example 7
# Specify multiple columns and moving those columns
# to the end of the dataframe
# Seed being used: #> ColumnRearrange TransactionID AccountID 4  --back 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

#> Visualize 
print(bankTransactionsDf.head()) #)13 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRearrange TransactionID AccountID 4  --back --example 
columnsToMove = ['TransactionID', 'AccountID', bankTransactionsDf.columns[4]]
columnsToMove = [column for column in bankTransactionsDf.columns if column not in columnsToMove] + columnsToMove
bankTransactionsDf = bankTransactionsDf[columnsToMove] 

#> Visualize 
print(bankTransactionsDf.head()) #)14 
##***    TransactionAmount     TransactionDate   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate TransactionID AccountID TransactionType
##*** 0              14.09 2023-04-11 16:29:14  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08      TX000001   AC00128           Debit
##*** 1             376.24 2023-06-27 16:44:19    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35      TX000002   AC00455           Debit
##*** 2             126.29 2023-07-10 18:16:08       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04      TX000003   AC00019           Debit
##*** 3             184.50 2023-05-05 16:32:11    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06      TX000004   AC00070           Debit
##*** 4              13.45 2023-10-16 17:51:24    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39      TX000005   AC00411          Credit
