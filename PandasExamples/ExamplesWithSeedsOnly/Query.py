
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Query for rows the meet a greater than / less than condition
# For Query, make sure to italicize column headers by placing
# underscores (_) on each side of the column name
# Seed being used: #> Query _Open_ > 150 
# ******************************************************
# ******************************************************

#> Visualize 

#> Query _Open_ > 150 

#> Visualize 



# Example 2
# Query for rows the meet two criteries with an "and" clause
# Seed being used: #> Query _Low_ > 100 and _High_ < 110 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 

#> Visualize 

#> Query _Low_ > 100 and _High_ < 110 

#> Visualize 



# Example 3
# Query for rows the meet two criteries with an "or" clause
# Also, this example shows querying with dates
# Seed being used: #> Query _Date_ > 2022 or _Low_ > 300 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data AppleStock.csv 

#> Visualize 

#> Query _Date_ > 2022 or _Low_ > 300 

#> Visualize 



# Example 3
# Query for fields where a string column contains a specified string
# Seed being used: #> Query _Location_ contains San 
# ******************************************************
# ******************************************************

# Load a different dataset with more string based columns
#> Data BankTransactions.csv 

#> Visualize 

#> Query _Location_ contains San 

#> Visualize 



# Example 4
# Query for fields where a string column end with a specified string
# You can do a similar query for starting with a string using "starts with"
# This also shows using variables in the query
# Seed being used: #> Query _DeviceID_ ends with endsWithValue 
# ******************************************************
# ******************************************************

# Reset the dataframe
#> Data BankTransactions.csv 

#> Visualize 

endsWithValue = "4"

#> Query _DeviceID_ ends with endsWithValue 

#> Visualize 



# Example 5
# More of a fuller example, this time, let's get the median of
# a column, and then find rows within 10% of the median
# Seed being used: #> Query _High_ > .9 * appleStockDfMedian and _High_ < 1.1 * appleStockDfMedian 
# ******************************************************
# ******************************************************

# We'll use the Apple stock data for this one
#> Data AppleStock.csv 

#> Visualize 

#> ColumnMedian High 

#> Query _High_ > .9 * appleStockDfMedian and _High_ < 1.1 * appleStockDfMedian 

#> Visualize 




