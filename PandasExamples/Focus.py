 
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
#> Focus appleStockDf --exampleTitle Set Focus to Previously Loaded Dataframe --example When working with multiple dataframes, it is often necessary to switch the focus from one to another. The Focus kit allows you to explicitly tell Arctic Fox which dataframe to apply subsequent transformations to. In this example, we load and modify two separate dataframes and then use Focus to return attention to appleStockDf so further kits act on it.
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

#> Focus ? --exampleTitle Get List of Variables for Focus Selection --example If you are unsure which dataframes or variables are currently available, the Focus kit can help. By using Focus with a question mark (?), you will active the guide which will show candidate variables to focus on. This makes it easier to select the correct target for subsequent operations.
#***Focus: Often, we perform consecutive operations on the same piece of data / dataframe. Because of this, Arctic Fox assumes that the most likely target is the most recently assigned dataframe. Sometimes though, we do wish to shift the target from the previously used dataframe to a different dataframe. Hence, the Focus kit, which specifies which dataframe to use for subsequent kits. Furthermore, if you are uncertain of the available variables, use the ? input and Focus will list the possible targets for you to select.
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


