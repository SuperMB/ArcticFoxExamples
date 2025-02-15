
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> VisualizeAllColumns 



# Example 1
# Switch focus to dataframe of interest
# Seed being used: #> Focus appleStockDf 
# ******************************************************
# ******************************************************

# Load in the first dataframe
#> Data AppleStock.csv 

# Do some operations on that dataframe
#> ColumnRemove 3 --throughLastColumn 

# See the result
#> Visualize 


# Switch to a new dataframe
#> Data BankTransactions.csv 

# See it's data
#> Visualize 


# Decide you want to switch back to the first dataframe
# Use the Focus seed to shift Arctic Fox's variable target
# back to the original dataframe
#> Focus appleStockDf 

# Do operations on the dataframe in focus
#> ColumnQuantile --columns High --quantile .25 .5 .6 .7 --variablesForQuantiles 



# Example 2
# Focus help gives you a list of variables to select from
# Seed being used: #> Focus ? 
# ******************************************************
# ******************************************************

# Load in other dataframes
#> Data Weather.csv 

#> Data Pizzerias.csv 

# Use Focus guide to get prepopulated list of variables
# to select from

#> Focus ? 




