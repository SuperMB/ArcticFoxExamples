 
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
# Remove a single column by column name
# Seed being used: #> ColumnRemove CustomerAge 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
#> ColumnRemove CustomerAge --exampleTitle Remove a Single Column --example Remove a single column from the dataframe by specifying its column name. This is helpful when a column is no longer needed in the analysis or is being removed to reduce dimensionality.
bankTransactionsDf.drop(columns='CustomerAge', inplace=True) 

#> Visualize 
print(bankTransactionsDf.head()) #)2 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online            Student                  198              1         7429.40     2024-11-04 08:06:39


# Example 2
# Remove multiple columns
# Seed being used: #> ColumnRemove TransactionID TransactionDuration 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRemove TransactionID TransactionDuration --exampleTitle Remove Multiple Columns by Name --example Remove more than one column at once by specifying the column names you want to drop. In this case, both TransactionID and TransactionDuration are removed from the dataframe.
bankTransactionsDf.drop(columns= ['TransactionID', 'TransactionDuration'] , inplace=True) 

#> Visualize 
print(bankTransactionsDf.head()) #)4 
##***   AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel CustomerOccupation  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM             Doctor              1         5112.21     2024-11-04 08:08:08
##*** 1   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM             Doctor              1        13758.91     2024-11-04 08:09:35
##*** 2   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online            Student              1         1122.35     2024-11-04 08:07:04
##*** 3   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online            Student              1         8569.06     2024-11-04 08:09:06
##*** 4   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online            Student              1         7429.40     2024-11-04 08:06:39



# Example 3
# Remove multiple columns by a mix of name and index
# Seed being used: #> ColumnRemove TransactionType 2 3 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***   AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel CustomerOccupation  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM             Doctor              1         5112.21     2024-11-04 08:08:08
##*** 1   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM             Doctor              1        13758.91     2024-11-04 08:09:35
##*** 2   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online            Student              1         1122.35     2024-11-04 08:07:04
##*** 3   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online            Student              1         8569.06     2024-11-04 08:09:06
##*** 4   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online            Student              1         7429.40     2024-11-04 08:06:39

#> ColumnRemove TransactionType 2 3 --exampleTitle Remove Columns by Name and Index --example You can remove columns by mixing column names and their index positions. In this example, we remove TransactionType by name and the columns at index 2 and 3 to eliminate specific features from the dataframe.
bankTransactionsDf.drop(columns= ['TransactionType', bankTransactionsDf.columns[2], bankTransactionsDf.columns[3]] , inplace=True) 

#> Visualize 
print(bankTransactionsDf.head()) #)6 
##***   AccountID  TransactionAmount   Location DeviceID      IP Address MerchantID Channel CustomerOccupation  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0   AC00128              14.09  San Diego  D000380  162.198.218.92       M015     ATM             Doctor              1         5112.21     2024-11-04 08:08:08
##*** 1   AC00455             376.24    Houston  D000051     13.149.61.4       M052     ATM             Doctor              1        13758.91     2024-11-04 08:09:35
##*** 2   AC00019             126.29       Mesa  D000235  215.97.143.157       M009  Online            Student              1         1122.35     2024-11-04 08:07:04
##*** 3   AC00070             184.50    Raleigh  D000187  200.13.225.150       M002  Online            Student              1         8569.06     2024-11-04 08:09:06
##*** 4   AC00411              13.45    Atlanta  D000308    65.164.3.100       M091  Online            Student              1         7429.40     2024-11-04 08:06:39



# Example 4
# Remove all non-numeric columns
# Seed being used: #> ColumnRemove --nonNumeric 
# ******************************************************
# ******************************************************

# Reset to the original dataframe
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

#> ColumnRemove --nonNumeric --exampleTitle Remove All Non-Numeric Columns --example If your analysis or model requires only numeric data, you can remove all columns that are not numeric. This operation filters the dataframe to retain only columns with numeric data types, such as integers or floats.
bankTransactionsDf = bankTransactionsDf.select_dtypes(include=['number']) 

#> Visualize 
print(bankTransactionsDf.head()) #)8 
##***    TransactionAmount  CustomerAge  TransactionDuration  LoginAttempts  AccountBalance
##*** 0              14.09           70                   81              1         5112.21
##*** 1             376.24           68                  141              1        13758.91
##*** 2             126.29           19                   56              1         1122.35
##*** 3             184.50           26                   25              1         8569.06
##*** 4              13.45           26                  198              1         7429.40
