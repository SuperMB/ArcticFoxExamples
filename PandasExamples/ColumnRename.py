 
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
# Fully rename a single column by column name
# Seed being used: #> ColumnRename CustomerAge --to Age 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
#> ColumnRename CustomerAge --to Age --example 
bankTransactionsDf = bankTransactionsDf.rename(columns={'CustomerAge': 'Age'}) 

#> Visualize 
print(bankTransactionsDf.head()) #)2 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  Age CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM   70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM   68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online   19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online   26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online   26            Student                  198              1         7429.40     2024-11-04 08:06:39


# Example 2
# Fully rename multiple columns by column name
# Seed being used: #> ColumnRename TransactionID AccountID --to tid aid 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  Age CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM   70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM   68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online   19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online   26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online   26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRename TransactionID AccountID --to tid aid --example 
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionID': 'tid', 'AccountID': 'aid'}) 

#> Visualize 
print(bankTransactionsDf.head()) #)4 
##***         tid      aid  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  Age CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0  TX000001  AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM   70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1  TX000002  AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM   68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2  TX000003  AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online   19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3  TX000004  AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online   26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4  TX000005  AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online   26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 3
# Fully rename multiple columns by column name and index
# Seed being used: #> ColumnRename TransactionDate 4 5  --to Date Payment City 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***         tid      aid  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  Age CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0  TX000001  AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM   70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1  TX000002  AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM   68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2  TX000003  AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online   19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3  TX000004  AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online   26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4  TX000005  AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online   26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnRename TransactionDate 4 5  --to Date Payment City --example 
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionDate': 'Date', bankTransactionsDf.columns[4]: 'Payment', bankTransactionsDf.columns[5]: 'City'}) 

#> Visualize 
print(bankTransactionsDf.head()) #)6 
##***         tid      aid  TransactionAmount                Date Payment       City DeviceID      IP Address MerchantID Channel  Age CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0  TX000001  AC00128              14.09 2023-04-11 16:29:14   Debit  San Diego  D000380  162.198.218.92       M015     ATM   70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1  TX000002  AC00455             376.24 2023-06-27 16:44:19   Debit    Houston  D000051     13.149.61.4       M052     ATM   68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2  TX000003  AC00019             126.29 2023-07-10 18:16:08   Debit       Mesa  D000235  215.97.143.157       M009  Online   19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3  TX000004  AC00070             184.50 2023-05-05 16:32:11   Debit    Raleigh  D000187  200.13.225.150       M002  Online   26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4  TX000005  AC00411              13.45 2023-10-16 17:51:24  Credit    Atlanta  D000308    65.164.3.100       M091  Online   26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 4
# Replace a matching piece of each column name with a new string/value
# Seed being used: #> ColumnRename --replace ID --with Identifier 
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

#> ColumnRename --replace ID --with Identifier --example 
bankTransactionsDf.columns = bankTransactionsDf.columns.str.replace('ID', 'Identifier') 

#> Visualize 
print(bankTransactionsDf.head()) #)8 
##***   TransactionIdentifier AccountIdentifier  TransactionAmount     TransactionDate TransactionType   Location DeviceIdentifier      IP Address MerchantIdentifier Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0              TX000001           AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego          D000380  162.198.218.92               M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1              TX000002           AC00455             376.24 2023-06-27 16:44:19           Debit    Houston          D000051     13.149.61.4               M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2              TX000003           AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa          D000235  215.97.143.157               M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3              TX000004           AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh          D000187  200.13.225.150               M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4              TX000005           AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta          D000308    65.164.3.100               M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 5
# Replace a matching piece of specified column names and index with a new string/value
# Seed being used: #> ColumnRename --columns TransactionAmount TransactionType --replace Transaction --with Payment 
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

#> ColumnRename --columns TransactionAmount TransactionType --replace Transaction --with Payment --example 
bankTransactionsDf = bankTransactionsDf.rename(columns={'TransactionAmount': 'TransactionAmount'.replace('Transaction', 'Payment'), 'TransactionType': 'TransactionType'.replace('Transaction', 'Payment')}) 

#> Visualize 
print(bankTransactionsDf.head()) #)10 
##***   TransactionID AccountID  PaymentAmount     TransactionDate PaymentType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128          14.09 2023-04-11 16:29:14       Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455         376.24 2023-06-27 16:44:19       Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019         126.29 2023-07-10 18:16:08       Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070         184.50 2023-05-05 16:32:11       Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411          13.45 2023-10-16 17:51:24      Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

