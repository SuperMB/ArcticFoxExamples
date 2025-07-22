 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 




# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> ColumnHeaders 
# Unnamed
# Date
# Open
# High
# Low
# Close
# Volume 



# Example 1
# Query for rows the meet a greater than / less than condition
# For Query, make sure to italicize column headers by placing
# underscores (_) on each side of the column name
# Seed being used: #> Query _Open_ > 150 
# ******************************************************
# ******************************************************

#> Visualize 
print(appleStockDf.head()) #)1 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Query _Open_ > 150 --exampleTitle Query with the Greater Than Operator --example Selects all rows where the value in the Open column is greater than 150. This is a common pattern for identifying records above a specified cutoff.
appleStockDf = appleStockDf[appleStockDf['Open'] > 150] 

#> Visualize 
print(appleStockDf.head()) #)2 
##***        Unnamed: 0       Date        Open        High         Low       Close    Volume
##*** 10266       10266 2021-08-31  150.319535  150.457388  148.970529  149.502258  86453100
##*** 10267       10267 2021-09-01  150.486915  152.603947  150.004422  150.171814  80313700
##*** 10268       10268 2021-09-02  151.510970  152.347945  150.063506  151.294342  71115500
##*** 10269       10269 2021-09-03  151.402658  152.259330  150.742931  151.934387  57808700
##*** 10270       10270 2021-09-07  152.594119  154.849004  152.023009  154.287750  82278300



# Example 2
# Query for rows the meet two criteries with an "and" clause
# Seed being used: #> Query _Low_ > 100 and _High_ < 110 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)3 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Query _Low_ > 100 and _High_ < 110 --exampleTitle Filter Rows Between Two Numeric Bounds --example Retrieves rows where Low is greater than 100 and High is less than 110. Combines two numeric conditions using AND logic to isolate a range of interest.
appleStockDf = appleStockDf[(appleStockDf['Low'] > 100) & (appleStockDf['High'] < 110)] 

#> Visualize 
print(appleStockDf.head()) #)4 
##***        Unnamed: 0       Date        Open        High         Low       Close     Volume
##*** 9994         9994 2020-08-03  105.669758  109.026873  105.369454  106.390015  308151200
##*** 9995         9995 2020-08-04  106.580453  108.199194  105.852872  107.100502  173071600
##*** 9996         9996 2020-08-05  106.819729  107.810993  106.350951  107.488708  121776800
##*** 10026       10026 2020-09-17  107.347399  109.773767  106.359237  107.953987  178011000
##*** 10027       10027 2020-09-18  108.012710  108.482326  103.795904  104.529686  287104900



# Example 3
# Query for rows the meet two criteries with an "or" clause
# Also, this example shows querying with dates
# Seed being used: #> Query _Date_ > 2022 or _Low_ > 300 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)5 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Query _Date_ > 2022 or _Low_ > 300 --exampleTitle Filter Rows with Mixed Conditions Using OR --example Applies a compound filter where either a date is after 2022 or a numeric value in Low exceeds 300. Demonstrates how to combine conditions across different column types.
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date'])
appleStockDf = appleStockDf[(appleStockDf['Date'].dt.year > 2022) | (appleStockDf['Low'] > 300)] 

#> Visualize 
print(appleStockDf.head()) #)6 
##***        Unnamed: 0       Date        Open        High         Low       Close     Volume
##*** 10352       10352 2022-01-03  175.359195  180.339032  175.240867  179.481110  104487900
##*** 10353       10353 2022-01-04  180.092499  180.398189  176.631258  177.203201   99310400
##*** 10354       10354 2022-01-05  177.114447  177.666664  172.213500  172.489609   94537600
##*** 10355       10355 2022-01-06  170.300485  172.864367  169.255216  169.610214   96904000
##*** 10356       10356 2022-01-07  170.487829  171.720462  168.653672  169.777832   86709100



# Example 3
# Query for fields where a string column contains a specified string
# Seed being used: #> Query _Location_ contains San 
# ******************************************************
# ******************************************************

# Load a different dataset with more string based columns
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

#> Query _Location_ contains San --exampleTitle Filter Rows by Substring Match in Text Columns --example Returns rows where the Location column contains the substring "San". Useful for partial string matching in text-based data.
bankTransactionsDf = bankTransactionsDf[bankTransactionsDf['Location'].astype('str').str.contains('San').fillna(False)] 

#> Visualize 
print(bankTransactionsDf.head()) #)8 
##***    TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0       TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 34      TX000035   AC00365             255.26 2023-10-27 16:42:49          Credit  San Francisco  D000357   92.214.76.157       M002  Branch           45             Doctor                   50              1        14815.87     2024-11-04 08:10:51
##*** 37      TX000038   AC00202             649.28 2023-03-02 17:53:32           Debit       San Jose  D000448   73.108.76.238       M074     ATM           75            Retired                  137              1         4875.86     2024-11-04 08:11:15
##*** 40      TX000041   AC00421             328.47 2023-07-31 18:39:50           Debit    San Antonio  D000557    6.234.101.35       M014     ATM           63            Retired                  119              1         4323.66     2024-11-04 08:07:31
##*** 53      TX000054   AC00055             169.50 2023-09-07 16:51:27           Debit      San Diego  D000442  42.219.228.159       M036  Branch           28            Student                  142              1          918.88     2024-11-04 08:08:58



# Example 4
# Query for fields where a string column end with a specified string
# You can do a similar query for starting with a string using "starts with"
# This also shows using variables in the query
# Seed being used: #> Query _DeviceID_ ends with endsWithValue 
# ******************************************************
# ******************************************************

# Reset the dataframe
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


#> Query _DeviceID_ ends with endsWithValue --exampleTitle Filter Rows Where Text Column Ends With a Specific Value --example Returns rows where the DeviceID column ends with a specific string. Demonstrates how to apply suffix-based matching for filtering text data.
bankTransactionsDf = bankTransactionsDf[bankTransactionsDf['DeviceID'].astype('str').str.endswith('endsWithValue').fillna(False)] 

#> Visualize 
print(bankTransactionsDf.head()) #)10 
##***    TransactionID AccountID  TransactionAmount     TransactionDate TransactionType      Location DeviceID       IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 13      TX000014   AC00264             781.76 2023-11-20 16:39:15           Debit       Memphis  D000054     193.83.0.183       M025     ATM           26            Student                  123              1          189.69     2024-11-04 08:07:06
##*** 48      TX000049   AC00296             626.90 2023-11-27 16:45:57           Debit        Denver  D000284    93.146.251.20       M023  Online           26            Student                  138              1          265.51     2024-11-04 08:07:24
##*** 49      TX000050   AC00471              22.01 2023-03-27 16:45:18          Credit    Sacramento  D000304     124.6.134.78       M055  Online           41           Engineer                  175              1         1335.09     2024-11-04 08:06:31
##*** 69      TX000070   AC00395             189.12 2023-11-13 16:42:28          Credit  Indianapolis  D000684   125.89.163.224       M040  Branch           32           Engineer                  103              1          977.01     2024-11-04 08:08:42
##*** 84      TX000085   AC00140             154.71 2023-07-03 16:40:24           Debit     San Diego  D000494  167.104.180.235       M030  Online           34             Doctor                  157              1         1523.72     2024-11-04 08:09:42



# Example 5
# More of a fuller example, this time, let's get the median of
# a column, and then find rows within 10% of the median
# Seed being used: #> Query _High_ > .9 * appleStockDfMedian and _High_ < 1.1 * appleStockDfMedian 
# ******************************************************
# ******************************************************

# We'll use the Apple stock data for this one
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> Visualize 
print(appleStockDf.head()) #)11 
##***    Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 0           0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1           1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2           2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3           3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4           4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> ColumnMedian High 
appleStockDfMedian = appleStockDf['High'].median() 

#> Query _High_ > .9 * appleStockDfMedian and _High_ < 1.1 * appleStockDfMedian --exampleTitle Filter Rows with Greater Than and Less Than Operators with Mathematical Operations --example In this example, we get the values that are within 10 percent above or below the median of the Apple stock.
appleStockDf = appleStockDf[(appleStockDf['High'] > .9 * appleStockDfMedian) & (appleStockDf['High'] < 1.1 * appleStockDfMedian)] 

#> Visualize 
print(appleStockDf.head()) #)12 
##***       Unnamed: 0       Date      Open      High       Low     Close     Volume
##*** 1714        1714 1987-09-24  0.381800  0.399939  0.381800  0.390437  182560000
##*** 1715        1715 1987-09-25  0.392165  0.400803  0.390437  0.397348  106523200
##*** 1716        1716 1987-09-28  0.397348  0.405986  0.383527  0.385255  203840000
##*** 1719        1719 1987-10-01  0.392165  0.405986  0.390437  0.402530  116480000
##*** 1720        1720 1987-10-02  0.402530  0.405986  0.397348  0.404258   96499200

