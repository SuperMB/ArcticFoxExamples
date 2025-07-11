 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 



# Setup
# ******************************************************
# ******************************************************

# None



# Example 1
# Switch focus to dataframe of interest
# Seed being used: #> Focus appleStockDf 
# ******************************************************
# ******************************************************

# Load in the first dataframe
#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

# Do some operations on that dataframe
#> ColumnRemove 3 --throughLastColumn 
appleStockDf.drop(columns=appleStockDf.columns[3:], axis=1, inplace=True) 

# See the result
#> Visualize 
print(appleStockDf.head()) #)1 


# Switch to a new dataframe
#> Data BankTransactions.csv 
bankTransactionsDf = pd.read_csv('BankTransactions.csv')
bankTransactionsDf['TransactionDate'] = pd.to_datetime(bankTransactionsDf['TransactionDate'])
bankTransactionsDf['PreviousTransactionDate'] = pd.to_datetime(bankTransactionsDf['PreviousTransactionDate']) 

# See it's data
#> Visualize 
print(bankTransactionsDf.head()) #)2 


# Decide you want to switch back to the first dataframe
# Use the Focus seed to shift Arctic Fox's variable target
# back to the original dataframe
#> Focus appleStockDf --example 
# Setting focus to appleStockDf 

# Do operations on the dataframe in focus
#> ColumnQuantile --columns High --quantile .25 .5 .6 .7 --variablesForQuantiles 
appleStockDfQuantile = appleStockDf['High'].quantile( [ .25, .5, .6, .7 ] )
appleStockDfQuantile0 = appleStockDfQuantile.iloc[0]
appleStockDfQuantile1 = appleStockDfQuantile.iloc[1]
appleStockDfQuantile2 = appleStockDfQuantile.iloc[2]
appleStockDfQuantile3 = appleStockDfQuantile.iloc[3] 



# Example 2
# Focus help gives you a list of variables to select from
# Seed being used: #> Focus ? 
# ******************************************************
# ******************************************************

# Load in other dataframes
#> Data Weather.csv 
weatherDf = pd.read_csv('Weather.csv') 

#> Data Pizzerias.csv 
pizzeriasDf = pd.read_csv('Pizzerias.csv') 

# Use Focus guide to get prepopulated list of variables
# to select from

#> Focus ? --example 
#***Focus: Changes the focus for following seeds to the specified dataframe or variable
#***
#***Please select which variable to make the Focus:
#***- appleStockDf #> `select appleStockDf
#***- bankTransactionsDf #> `select bankTransactionsDf
#***- appleStockDfQuantile #> `select appleStockDfQuantile
#***- appleStockDfQuantile0 #> `select appleStockDfQuantile0
#***- appleStockDfQuantile1 #> `select appleStockDfQuantile1
#***- appleStockDfQuantile2 #> `select appleStockDfQuantile2
#***- appleStockDfQuantile3 #> `select appleStockDfQuantile3
#***- weatherDf #> `select weatherDf
#***- pizzeriasDf #> `select pizzeriasDf


