 
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
# Get the default quantiles of a single column
# Seed being used: #> ColumnQuantile CustomerAge 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
#> ColumnQuantile CustomerAge --exampleTitle Get Default Quantile of a Single Column --example By default, quantile returns the median (0.5 quantile) when no specific value is provided. In this example, we compute the median CustomerAge to understand the central tendency of the column.
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile() 

#> print 
print(bankTransactionsDfQuantile) #)2 
##*** 45.0



# Example 2
# Get the quantiles of a single column and specify what
# quantiles to get
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 
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

#> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --exampleTitle Get Specific Quantiles of a Single Column --example Rather than just retrieving the default median, we can specify the exact quantiles we want. Here we calculate the 25%, 50%, 75%, and 100% of CustomerAge to better understand its distribution.
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile( [ .25, .5, .75, 1 ] ) 

#> print 
print(bankTransactionsDfQuantile) #)4 
##*** 0.25    27.0
##*** 0.50    45.0
##*** 0.75    59.0
##*** 1.00    80.0
##*** Name: CustomerAge, dtype: float64



# Example 3
# Get the quantiles of a single column, specify what quantiles
# to get, and create a variable for each
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles --exampleTitle Create Variables for Each Quantile --example In addition to computing quantiles, we can assign each quantile value to its own variable. This allows for easier use later in code when comparing or referencing specific thresholds.
bankTransactionsDfQuantile = bankTransactionsDf['CustomerAge'].quantile( [ .25, .5, .75, 1 ] )
bankTransactionsDfQuantile0 = bankTransactionsDfQuantile.iloc[0]
bankTransactionsDfQuantile1 = bankTransactionsDfQuantile.iloc[1]
bankTransactionsDfQuantile2 = bankTransactionsDfQuantile.iloc[2]
bankTransactionsDfQuantile3 = bankTransactionsDfQuantile.iloc[3] 

#> print bankTransactionsDfQuantile 
print(bankTransactionsDfQuantile) #)6 
##*** 0.25    27.0
##*** 0.50    45.0
##*** 0.75    59.0
##*** 1.00    80.0
##*** Name: CustomerAge, dtype: float64

#> print bankTransactionsDfQuantile0 
print(bankTransactionsDfQuantile0) #)7 
##*** 27.0

#> print bankTransactionsDfQuantile1 
print(bankTransactionsDfQuantile1) #)8 
##*** 45.0

#> print bankTransactionsDfQuantile2 
print(bankTransactionsDfQuantile2) #)9 
##*** 59.0

#> print bankTransactionsDfQuantile3 
print(bankTransactionsDfQuantile3) #)10 
##*** 80.0



# Example 4
# Get the default quantile of multiple columns
# Seed being used: #> ColumnQuantile AccountBalance TransactionDuration 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)11 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnQuantile AccountBalance TransactionDuration --exampleTitle Get Default Quantile of Multiple Columns --example When multiple columns are passed without specifying a quantile, the default behavior is to compute the 0.5 quantile (median) for each. This provides a quick snapshot of the central values across several numerical features.
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDuration'] ].quantile() 

#> print 
print(bankTransactionsDfQuantile) #)12 
##*** AccountBalance         4735.51
##*** TransactionDuration     112.50
##*** Name: 0.5, dtype: float64



# Example 5
# Get the quantiles of a multiple columns and specify what
# quantiles to get
# Seed being used: #> ColumnQuantile --columns AccountBalance TransactionDate --quantile .2 .4 .6 .8 1 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)13 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnQuantile --columns AccountBalance TransactionDate --quantile .2 .4 .6 .8 1 --exampleTitle Get Specific Quantiles Across Multiple Columns --example You can compute specific quantiles for multiple columns at once. This example includes both numeric and datetime data types to show how quantiles are calculated consistently across supported types.
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDate'] ].quantile( [ .2, .4, .6, .8, 1 ] ) 

#> print 
print(bankTransactionsDfQuantile) #)14 
##***      AccountBalance         TransactionDate
##*** 0.2        1236.908 2023-03-13 16:32:31.400
##*** 0.4        3022.536 2023-06-01 16:31:45.800
##*** 0.6        6055.736 2023-08-14 17:04:29.000
##*** 0.8        8461.020 2023-10-23 16:50:01.600
##*** 1.0       14977.990 2024-01-01 18:21:50.000



# Example 6
# Get the quantiles of a single column, specify what quantiles
# to get, and create a variable for each
# Seed being used: #> ColumnQuantile --columns CustomerAge --quantile .25 .5 .75 1 --variablesForQuantiles 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)15 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ColumnQuantile --columns AccountBalance TransactionDuration --quantile .3 .6 .9 --variablesForQuantiles --exampleTitle Store Quantiles of Multiple Columns in Separate Variables --example After computing several quantiles across multiple columns, you can create separate variables for each quantile-column combination. This enables fine-grained control over how the results are used later in the analysis or logic flow.
bankTransactionsDfQuantile = bankTransactionsDf [ ['AccountBalance', 'TransactionDuration'] ].quantile( [ .3, .6, .9 ] )
bankTransactionsDfQuantile_AccountBalance_0 = bankTransactionsDfQuantile.iloc[0]['AccountBalance']
bankTransactionsDfQuantile_AccountBalance_1 = bankTransactionsDfQuantile.iloc[1]['AccountBalance']
bankTransactionsDfQuantile_AccountBalance_2 = bankTransactionsDfQuantile.iloc[2]['AccountBalance']
bankTransactionsDfQuantile_TransactionDuration_0 = bankTransactionsDfQuantile.iloc[0]['TransactionDuration']
bankTransactionsDfQuantile_TransactionDuration_1 = bankTransactionsDfQuantile.iloc[1]['TransactionDuration']
bankTransactionsDfQuantile_TransactionDuration_2 = bankTransactionsDfQuantile.iloc[2]['TransactionDuration'] 

