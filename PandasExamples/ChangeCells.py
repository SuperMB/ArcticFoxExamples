 
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




# Example 1
# Change AccountID in rows 2, 4, and 5 to Inactive
# Seed being used: #> ChangeCells --rows 2 4 5 --columns AccountID --value Inactive 
# ******************************************************
# ******************************************************

#> Visualize --count 6 
print(bankTransactionsDf.head(n=6)) #)1 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
##*** 5      TX000006   AC00393              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579  117.67.192.211       M054     ATM           18            Student                  172              1          781.68     2024-11-04 08:06:36

#> ChangeCells --rows 2 4 5 --columns AccountID --value Inactive --exampleTitle Change Cell by Row and Column --example Change specific rows within one or more columns to a new value. In this case, in the column AcountID we are changing rows with index 2, 4, and 5 to Inactive to mark that those accounts are no longer used. 
bankTransactionsDf.loc[[2, 4, 5], 'AccountID' ] = 'Inactive' 

#> Visualize --count 6 
print(bankTransactionsDf.head(n=6)) #)2 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType       Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit      San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit        Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003  Inactive             126.29 2023-07-10 18:16:08           Debit           Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit        Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005  Inactive              13.45 2023-10-16 17:51:24          Credit        Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
##*** 5      TX000006  Inactive              92.15 2023-04-03 17:15:01           Debit  Oklahoma City  D000579  117.67.192.211       M054     ATM           18            Student                  172              1          781.68     2024-11-04 08:06:36



# Example 2
# Change occurences of San Diego to Los Angeles in the Location column
# Seed being used: #> ChangeCells --initialValues San  Diego --newValues Los  Angeles --columns Location 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType   Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  San Diego  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit    Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003  Inactive             126.29 2023-07-10 18:16:08           Debit       Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit    Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005  Inactive              13.45 2023-10-16 17:51:24          Credit    Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ChangeCells --initialValues San  Diego --newValues Los  Angeles --columns Location --exampleTitle Change Cells by String Match and Replace --example Modify all cells in a column that match a given string with a new value. In this case, we want to replace San Diego with Los Angeles in the column Location. If the entire cell was San Diego, than the entire cell would be change to Los Angeles. However, if the cell contained other text in addition to San Diego, the other text would remain the same, and only San Diego in the cell would change to Los Angeles. 
bankTransactionsDf['Location'] = bankTransactionsDf['Location'].str.replace('San Diego', 'Los Angeles') 

#> Visualize 
print(bankTransactionsDf.head()) #)4 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType     Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  Los Angeles  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit      Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003  Inactive             126.29 2023-07-10 18:16:08           Debit         Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit      Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005  Inactive              13.45 2023-10-16 17:51:24          Credit      Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39



# Example 3
# Change transactions after June 1st 2023 to be of TransactionType cash
# This illustrates changing only cells that meet a stated criteria
# Seed being used: #> ChangeCells --columns TransactionType --value Cash --where _TransactionDate_ > 06-01-2023 --allMatchingRows 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)5 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType     Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  Los Angeles  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19           Debit      Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003  Inactive             126.29 2023-07-10 18:16:08           Debit         Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit      Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005  Inactive              13.45 2023-10-16 17:51:24          Credit      Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39

#> ChangeCells --columns TransactionType --value Cash --where _TransactionDate_ > 06-01-2023 --allMatchingRows --exampleTitle Change Cells That Meet Condition --example Set all cells in a column to a new value if the cell meets the desired condition. Here, the condition is that the TransactionDate in a row is after (greater than) 06-01-2023. Therefore, if the TransactionDate is after 06-01-2023, then we set the TransactionType cell to Cash in the row. This would replace then entire contents of the cell TransactionType in the row. 
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf.loc[ bankTransactionsDf['TransactionDate'] > "06 - 01 - 2023", 'TransactionType' ] = 'Cash' 

#> Visualize 
print(bankTransactionsDf.head()) #)6 
##***   TransactionID AccountID  TransactionAmount     TransactionDate TransactionType     Location DeviceID      IP Address MerchantID Channel  CustomerAge CustomerOccupation  TransactionDuration  LoginAttempts  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128              14.09 2023-04-11 16:29:14           Debit  Los Angeles  D000380  162.198.218.92       M015     ATM           70             Doctor                   81              1         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455             376.24 2023-06-27 16:44:19            Cash      Houston  D000051     13.149.61.4       M052     ATM           68             Doctor                  141              1        13758.91     2024-11-04 08:09:35
##*** 2      TX000003  Inactive             126.29 2023-07-10 18:16:08            Cash         Mesa  D000235  215.97.143.157       M009  Online           19            Student                   56              1         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070             184.50 2023-05-05 16:32:11           Debit      Raleigh  D000187  200.13.225.150       M002  Online           26            Student                   25              1         8569.06     2024-11-04 08:09:06
##*** 4      TX000005  Inactive              13.45 2023-10-16 17:51:24            Cash      Atlanta  D000308    65.164.3.100       M091  Online           26            Student                  198              1         7429.40     2024-11-04 08:06:39
