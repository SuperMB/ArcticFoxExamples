
import random
import pandas as pd
import numpy as np

#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')


#> ColumnGet --columns Location 
location_1 = bankTransactionsDf['Location'] 
location = bankTransactionsDf['Location']

# Example 1 Add location as a new column

#> ColumnAdd location 
#***Analyze location to learn about: type
#***#> `run script and gather data 
# User changes detected
bankTransactionsDf['new_location'] = location

#> Random --list --count 2512 
randomList_1 = [random.random() for ___1 in range(2512)] 
randomList = [random.random() for __ in range(2512)]

#> ToSeries 
randomListSeries = pd.Series(randomList) 
randomListSeries = pd.Series(randomList)

#Example 2 Add random series to the dataframe
#> ColumnAdd randomListSeries 
#***Analyze randomListSeries to learn about: type
#***#> `run script and gather data 
bankTransactionsDf['randomListSeries'] = randomListSeries

