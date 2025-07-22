 
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

# Get some of the columns from the data frame
#> ColumnGet --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 
location = bankTransactionsDf['Location']
deviceID = bankTransactionsDf['DeviceID']
iPAddress = bankTransactionsDf['IP Address']
transactionDuration = bankTransactionsDf['TransactionDuration']
loginAttempts = bankTransactionsDf['LoginAttempts'] 

# Then, remove those columns
#> ColumnRemove --columns Location DeviceID IP  Address TransactionDuration LoginAttempts 
bankTransactionsDf.drop(columns= ['Location', 'DeviceID', 'IP Address', 'TransactionDuration', 'LoginAttempts'] , inplace=True) 



# Example 1
# Add new empty column
# Seed being used: #> ColumnAdd --newColumnNames NewEmptyColumn 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)1 

#> ColumnAdd --newColumnNames NewEmptyColumn --exampleTitle Add a New Empty Column --example Add an empty column to a dataframe that has a desired column name. Specify the desired column name with the --exampleTitle option. Each row will have a missing value for the new column. 
bankTransactionsDf['NewEmptyColumn'] = pd.Series() 

#> Visualize 
print(bankTransactionsDf.head()) #)2 



# Example 2
# Add a column with a default value
# Seed being used: #> ColumnAdd 1 --newColumnNames Columnof1s 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)3 

#> ColumnAdd 1 --newColumnNames Columnof1s --exampleTitle Added a Column With Set Value --example Add a column to the dataframe where every row in the column has the same value. In this case, the column name is Columnof1s and the value of each row for the column will be 1 
bankTransactionsDf['Columnof1s'] = 1 

#> Visualize 
print(bankTransactionsDf.head()) #)4 



# Example 3
# Add location, which is a series previously extracted, as a new column
# Seed being used: #> ColumnAdd location 
# ******************************************************
# ******************************************************

#> Visualize 
print(bankTransactionsDf.head()) #)5 

#> ColumnAdd location --exampleTitle Adding a Variable as a Column --example Add a variable as a column to the dataframe. If a column name is not provided, the column name will be the same as the variable name. Here, the variable location is added to the dataframe as a new column names location.
bankTransactionsDf['location'] = location 

#> Visualize 
print(bankTransactionsDf.head()) #)6 


