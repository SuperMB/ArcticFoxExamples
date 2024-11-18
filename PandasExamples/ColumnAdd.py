#>1
import random
import pandas as pd
import numpy as np#<1

#⮞ Data BankTransactions.csv ⮜#@>2
bankTransactionsDf = pd.read_csv('../BankTransactions.csv')#<2


#⮞ ColumnGet --columns Location ⮜#@>3
location = bankTransactionsDf['Location']#<3

# Example 1 Add location as a new column

#⮞ ColumnAdd location ⮜#@>4
# User changes detected
bankTransactionsDf['new_location'] = location#<4

#⮞ Random --list --count 2512 ⮜#@>5
randomList = [random.random() for __ in range(2512)]#<5

#⮞ ToSeries  ⮜#@>6
randomListSeries = pd.Series(randomList)#<6

#Example 2 Add random series to the dataframe
#⮞ ColumnAdd randomListSeries ⮜#@>7
bankTransactionsDf['randomListSeries'] = randomListSeries#<7

