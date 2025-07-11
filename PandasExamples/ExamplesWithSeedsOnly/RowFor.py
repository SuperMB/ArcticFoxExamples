
#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Iterate over the rows to find the max difference between
# the High and Low columns. RowFor creates the for loop that
# iterates over the rows, the rest of the code in the for loop
# is written by the user, not Arctic Fox.
# Seed being used: #> RowFor 
# ******************************************************
# ******************************************************

#> Visualize 

maxDifference = -100000
#> RowFor 
# User changes detected
for index, row in appleStockDf.iterrows():
    maxDifference = max(maxDifference, row['High'] - row['Low'])

#> print 



