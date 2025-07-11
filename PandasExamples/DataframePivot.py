 
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
# Pivoting a table to sum one column according to the categories of another column
# This pivot only uses rows, no columns for the resulting table
# Seed being used: #> DataframePivot --rows Location --cells TransactionAmount --sum 
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

#> DataframePivot --rows Location --cells TransactionAmount --sum --example 
bankTransactionsDfPivot = bankTransactionsDf.pivot_table(index='Location', values='TransactionAmount', aggfunc='sum') 

#> print 
print(bankTransactionsDfPivot) #)2 
##***                   TransactionAmount
##*** Location
##*** Albuquerque                10214.09
##*** Atlanta                    16052.26
##*** Austin                     22740.90
##*** Baltimore                  15154.46
##*** Boston                     16793.23
##*** Charlotte                  17682.66
##*** Chicago                    16225.82
##*** Colorado Springs           20344.63
##*** Columbus                   19079.18
##*** Dallas                     10888.19
##*** Denver                     15661.74
##*** Detroit                    20609.76
##*** El Paso                    16997.55
##*** Fort Worth                 20776.74
##*** Fresno                     13390.95
##*** Houston                    19416.65
##*** Indianapolis               16522.97
##*** Jacksonville               20519.47
##*** Kansas City                18768.50
##*** Las Vegas                  16428.33
##*** Los Angeles                19675.75
##*** Louisville                 13505.10
##*** Memphis                    21170.53
##*** Mesa                       19163.64
##*** Miami                      16969.23
##*** Milwaukee                  15235.14
##*** Nashville                  14532.52
##*** New York                   17640.23
##*** Oklahoma City              21716.04
##*** Omaha                      18404.35
##*** Philadelphia               19469.32
##*** Phoenix                    19064.66
##*** Portland                   14222.11
##*** Raleigh                    17101.97
##*** Sacramento                 12974.50
##*** San Antonio                19323.13
##*** San Diego                  19222.41
##*** San Francisco              16840.64
##*** San Jose                   20127.87
##*** Seattle                    14440.09
##*** Tucson                     20459.76
##*** Virginia Beach             15178.96
##*** Washington                 16849.54



# Example 2
# Pivoting a table get the max of one column according to the categories of two
# other columns. This pivot uses both rows and columns for the resulting table
# Seed being used: #> DataframePivot --rows Location --columns TransactionType --cells AccountBalance --max 
# ******************************************************
# ******************************************************

# Refocus on the original dataframe
#> Focus bankTransactionsDf 
# Setting focus to bankTransactionsDf 

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> DataframePivot --rows Location --columns TransactionType --cells AccountBalance --max --example 
bankTransactionsDfPivot = bankTransactionsDf.pivot_table(index='Location', columns='TransactionType', values='AccountBalance', aggfunc='max') 

#> print 
print(bankTransactionsDfPivot) #)4 
##*** TransactionType     Credit     Debit
##*** Location
##*** Albuquerque       14765.41  14563.02
##*** Atlanta           14935.50  12801.93
##*** Austin            13546.75  13538.14
##*** Baltimore          9700.90  12893.85
##*** Boston            12578.75  14350.11
##*** Charlotte         13357.02  14453.35
##*** Chicago           12272.78  14510.80
##*** Colorado Springs  12690.79  13648.36
##*** Columbus          13645.63  13486.15
##*** Dallas            14489.69  14473.33
##*** Denver            14389.45  12221.17
##*** Detroit           11989.39  14466.38
##*** El Paso            9383.43  14851.28
##*** Fort Worth        11079.77  14942.78
##*** Fresno             9895.10  14348.65
##*** Houston           14881.77  14829.85
##*** Indianapolis      12991.03  14268.95
##*** Jacksonville      13267.09  14343.00
##*** Kansas City        8551.60  14328.29
##*** Las Vegas         14798.10  14371.08
##*** Los Angeles       11385.37  14365.18
##*** Louisville        11538.97  14631.88
##*** Memphis           13869.86  14494.18
##*** Mesa              13625.52  12995.70
##*** Miami              8441.61  10790.80
##*** Milwaukee         12467.31  14676.05
##*** Nashville         12071.10  13265.92
##*** New York          12719.93   9873.62
##*** Oklahoma City     13558.56  13793.53
##*** Omaha             10156.09  13891.47
##*** Philadelphia      12500.80  14464.30
##*** Phoenix           12709.58  14804.70
##*** Portland           9381.64  13531.22
##*** Raleigh            7764.16  14817.22
##*** Sacramento        14847.97  13542.41
##*** San Antonio       14180.21  12626.49
##*** San Diego         12883.91  14611.90
##*** San Francisco     14815.87  13732.81
##*** San Jose          14833.34  14977.99
##*** Seattle           13316.71  14410.44
##*** Tucson            13704.92  14021.40
##*** Virginia Beach    10456.24  14928.35
##*** Washington         9927.75  13374.89



# Example 3
# Pivoting a table get the count of occurences of multiple columns.
# This pivot uses both rows and columns for the resulting table, and
# uses two columns for the new columns of the pivot.
# Seed being used: #> DataframePivot --rows Location --cells TransactionAmount --sum 
# ******************************************************
# ******************************************************

# Change focus to original dataframe
#> Focus bankTransactionsDf 
# Setting focus to bankTransactionsDf 

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> DataframePivot --rows Location --columns Channel TransactionType --cells AccountID --count --example 
bankTransactionsDfPivot = bankTransactionsDf.pivot_table(index='Location', columns= [ 'Channel', 'TransactionType' ] , values='AccountID', aggfunc='count') 

#> print 
print(bankTransactionsDfPivot) #)6 
##*** Channel             ATM       Branch       Online
##*** TransactionType  Credit Debit Credit Debit Credit Debit
##*** Location
##*** Albuquerque         NaN  12.0    6.0   7.0    4.0  12.0
##*** Atlanta             1.0  15.0    8.0  15.0    5.0  17.0
##*** Austin              2.0   9.0   13.0  13.0    8.0  14.0
##*** Baltimore           2.0  18.0    4.0  13.0    5.0   9.0
##*** Boston              1.0  21.0    8.0   9.0    4.0  18.0
##*** Charlotte           2.0  19.0    4.0  19.0    4.0  20.0
##*** Chicago             1.0  17.0    5.0  12.0    5.0  20.0
##*** Colorado Springs    1.0  22.0    6.0  15.0    4.0  12.0
##*** Columbus            1.0  17.0    5.0  13.0    3.0  15.0
##*** Dallas              3.0  15.0    5.0  13.0    3.0  10.0
##*** Denver              1.0  23.0    5.0  16.0    4.0  13.0
##*** Detroit             2.0  16.0    4.0  20.0    8.0  13.0
##*** El Paso             NaN  20.0    3.0  10.0    2.0  11.0
##*** Fort Worth          1.0  29.0    8.0  13.0    6.0  13.0
##*** Fresno              3.0  16.0    4.0  19.0    6.0  12.0
##*** Houston             NaN  18.0    6.0  18.0    8.0  13.0
##*** Indianapolis        1.0  21.0    8.0  13.0    6.0   9.0
##*** Jacksonville        2.0  18.0    6.0  14.0   10.0  10.0
##*** Kansas City         1.0  18.0    8.0  15.0    4.0  15.0
##*** Las Vegas           1.0  14.0    4.0  12.0    5.0  19.0
##*** Los Angeles         3.0  23.0    7.0  21.0    5.0  10.0
##*** Louisville          1.0  10.0    6.0  18.0    5.0  11.0
##*** Memphis             1.0  20.0    9.0   9.0    7.0  17.0
##*** Mesa                1.0  25.0    7.0  14.0    5.0   9.0
##*** Miami               2.0  17.0    4.0  17.0    5.0  19.0
##*** Milwaukee           3.0  19.0    3.0  12.0    6.0  12.0
##*** Nashville           NaN  19.0    9.0  14.0    7.0   6.0
##*** New York            1.0  12.0    7.0  18.0    5.0  15.0
##*** Oklahoma City       2.0  22.0    6.0  16.0    7.0  15.0
##*** Omaha               2.0  28.0    7.0  12.0    5.0  11.0
##*** Philadelphia        3.0  17.0   10.0  17.0    6.0  14.0
##*** Phoenix             3.0  17.0    2.0  13.0    6.0  14.0
##*** Portland            3.0  12.0    3.0   9.0    5.0  10.0
##*** Raleigh             4.0  16.0    3.0  20.0    6.0  10.0
##*** Sacramento          3.0  13.0    7.0  12.0    7.0  11.0
##*** San Antonio         4.0  22.0    3.0  13.0    5.0  12.0
##*** San Diego           2.0  15.0    3.0  14.0   10.0  15.0
##*** San Francisco       1.0  19.0    6.0  13.0    5.0  13.0
##*** San Jose            2.0  18.0    9.0  13.0    5.0  12.0
##*** Seattle             2.0  16.0    3.0  14.0    9.0  17.0
##*** Tucson              2.0  18.0    5.0  22.0    6.0  14.0
##*** Virginia Beach      2.0  12.0    8.0  13.0    7.0  13.0
##*** Washington          NaN  12.0    4.0  14.0    6.0  12.0



# Example 4
# Pivoting a table get the sum of a column with multiple columns
# being used for both the rows and columns of the pivoted table.
# Seed being used: #> DataframePivot --rows CustomerAge TransactionType --columns Channel LoginAttempts CustomerOccupation --cells TransactionAmount --sum 
# ******************************************************
# ******************************************************

# Change focus to original dataframe
#> Focus bankTransactionsDf 
# Setting focus to bankTransactionsDf 

#> Visualize 
print(bankTransactionsDf.head()) #)7 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> DataframePivot --rows CustomerAge TransactionType --columns Channel LoginAttempts CustomerOccupation --cells TransactionAmount --sum --example 
bankTransactionsDfPivot = bankTransactionsDf.pivot_table(index= [ 'CustomerAge', 'TransactionType' ] , columns= [ 'Channel', 'LoginAttempts', 'CustomerOccupation' ] , values='TransactionAmount', aggfunc='sum') 

#> print 
print(bankTransactionsDfPivot) #)8 
##*** Channel                        ATM                                                                                                                                            Branch                                                                                                                                                    Online
##*** LoginAttempts                    1                                 2                               3                       4                       5                               1                                 2                               3                       4                               5                               1                                 2                       3                               4                                5
##*** CustomerOccupation          Doctor Engineer  Retired  Student Doctor Engineer Retired Student Doctor Engineer Student Doctor Engineer Student Doctor Engineer Retired Student Doctor Engineer  Retired  Student Doctor Engineer Retired Student Doctor Engineer Student Doctor Engineer Retired Student Doctor Engineer Retired Student Doctor Engineer  Retired  Student Doctor Engineer Retired Doctor Engineer Retired Student Doctor Engineer Retired  Student Doctor Retired Student
##*** CustomerAge TransactionType
##*** 18          Credit             NaN      NaN      NaN   242.39    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN   353.82    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN  1666.32    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##***             Debit              NaN      NaN      NaN  6226.98    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN  5068.33    NaN      NaN     NaN  120.24    NaN      NaN     NaN    NaN      NaN     NaN  142.19    NaN      NaN     NaN     NaN    NaN      NaN      NaN  1699.11    NaN      NaN     NaN    NaN      NaN     NaN   13.48    NaN      NaN     NaN  1531.31    NaN     NaN     NaN
##*** 19          Credit             NaN      NaN      NaN   757.01    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN   886.30    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN   127.0    NaN      NaN      NaN  1569.73    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##***             Debit              NaN      NaN      NaN  5544.65    NaN      NaN     NaN  307.24    NaN      NaN  139.57    NaN      NaN  238.54    NaN      NaN     NaN     NaN    NaN      NaN      NaN  3865.08    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN  7193.75    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##*** 20          Credit             NaN      NaN      NaN   270.54    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN  3203.49    NaN      NaN     NaN  308.85    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN      NaN   364.93    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##*** ...                            ...      ...      ...      ...    ...      ...     ...     ...    ...      ...     ...    ...      ...     ...    ...      ...     ...     ...    ...      ...      ...      ...    ...      ...     ...     ...    ...      ...     ...    ...      ...     ...     ...    ...      ...     ...     ...    ...      ...      ...      ...    ...      ...     ...    ...      ...     ...     ...    ...      ...     ...      ...    ...     ...     ...
##*** 78          Debit              NaN      NaN  2195.80      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN  1742.05      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN  1713.55      NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN  337.73      NaN    NaN     NaN     NaN
##*** 79          Credit             NaN      NaN      NaN      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN  1597.14      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN   192.02      NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN   66.90      NaN    NaN     NaN     NaN
##***             Debit              NaN      NaN  1347.68      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN  2977.64      NaN    NaN      NaN  263.99     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN   928.73      NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##*** 80          Credit             NaN      NaN      NaN      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN    27.07      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN   557.41      NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN     NaN     NaN
##***             Debit              NaN      NaN  2950.42      NaN    NaN      NaN  351.99     NaN    NaN      NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN   876.95      NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     6.3     NaN    NaN      NaN   244.96      NaN    NaN      NaN     NaN    NaN      NaN     NaN     NaN    NaN      NaN     NaN      NaN    NaN  302.16     NaN
##***
##*** [126 rows x 55 columns]
