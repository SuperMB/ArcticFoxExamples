 
import pandas as pd
import numpy as np  
pd.set_option('display.max_rows', None)  
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
# Show all rows in the dataframe from the Visualize ssed.
# Without, Visualize will show a portion of the rows.
# However, use with caution to not display very large dataframes.
# Seed being used: #> VisualizeAllRows 
# ******************************************************
# ******************************************************

#> VisualizeAllRows --exampleTitle View All Rows In a Dataframe --example Use this kit with caution!! This will cause any Visualize kits to display all of the rows of a dataframe, which may be thousands! And, this will print the result into the file when using the visualize kits. This kit has its uses, just use carefully!
# !!!*** USE WITH CAUTION ***!!!
# Code added to start of file to display all rows for dataframes 

# Remove all but the first 100 rows so the dataframe isn't too large
#> RowRemove --indexStart 100 
bankTransactionsDf = bankTransactionsDf.drop(bankTransactionsDf.index[100:]) 

#> Visualize 
print(bankTransactionsDf.head()) #)1 
##***   TransactionID AccountID  ...  AccountBalance PreviousTransactionDate
##*** 0      TX000001   AC00128  ...         5112.21     2024-11-04 08:08:08
##*** 1      TX000002   AC00455  ...        13758.91     2024-11-04 08:09:35
##*** 2      TX000003   AC00019  ...         1122.35     2024-11-04 08:07:04
##*** 3      TX000004   AC00070  ...         8569.06     2024-11-04 08:09:06
##*** 4      TX000005   AC00411  ...         7429.40     2024-11-04 08:06:39
##***
##*** [5 rows x 16 columns]


