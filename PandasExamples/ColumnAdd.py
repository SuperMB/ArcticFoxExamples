
import random
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

# Get some of the columns from the data frame
#> ColumnGet --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 
location = bankTransactionsDf['Location']
deviceID = bankTransactionsDf['DeviceID']
iPAddress = bankTransactionsDf['IP Address']
transactionDuration = bankTransactionsDf['TransactionDuration']
loginAttempts = bankTransactionsDf['LoginAttempts'] 

# Then, remove those columns
#> ColumnRemove --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 



# Example 1
# Add new empty column
# Seed being used: #> ColumnAdd --newColumnNames NewEmptyColumn 
# ******************************************************
# ******************************************************

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39

#> ColumnAdd --newColumnNames NewEmptyColumn 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN



# Example 2
# Add a column with a default value
# Seed being used: #> ColumnAdd 1 --newColumnNames Columnof1s 
# ******************************************************
# ******************************************************

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN

#> ColumnAdd 1 --newColumnNames Columnof1s 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn  Columnof1s
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN           1
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN           1
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN           1
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN           1
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN           1



# Example 3
# Add location, which is a series previously extracted, as a new column
# Seed being used: #> ColumnAdd location 
# ******************************************************
# ******************************************************

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn  Columnof1s
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN           1
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN           1
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN           1
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN           1
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN           1

#> ColumnAdd location 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn  Columnof1s   location
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN           1  San Diego
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN           1    Houston
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN           1       Mesa
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN           1    Raleigh
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN           1    Atlanta



# Example 4
# Add a random series to the dataframe
# Seed being used: #> ColumnAdd randomListSeries 
# ******************************************************
# ******************************************************

#> Visualize 
#***Analyze loginAttempts to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn  Columnof1s   location
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN           1  San Diego
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN           1    Houston
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN           1       Mesa
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN           1    Raleigh
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN           1    Atlanta

#> Random --list --count 2512 
randomList = [random.random() for __ in range(2512)] 

#> ToSeries 
#***Analyze randomList to learn about: type
#***#> `run script and gather data 

#> ColumnAdd randomListSeries 
#***Analyze randomList to learn about: type
#***#> `run script and gather data 

#> Visualize 
#***Analyze randomList to learn about: type
#***#> `run script and gather data 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType MerchantID Channel  CustomerAge CustomerOccupation  AccountBalance PreviousTransactionDate NewEmptyColumn  Columnof1s   location  randomListSeries
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit       M015     ATM           70             Doctor         5112.21     2024-11-04 08:08:08            NaN           1  San Diego          0.848532
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit       M052     ATM           68             Doctor        13758.91     2024-11-04 08:09:35            NaN           1    Houston          0.197302
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       M009  Online           19            Student         1122.35     2024-11-04 08:07:04            NaN           1       Mesa          0.373826
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit       M002  Online           26            Student         8569.06     2024-11-04 08:09:06            NaN           1    Raleigh          0.822673
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit       M091  Online           26            Student         7429.40     2024-11-04 08:06:39            NaN           1    Atlanta          0.001565
