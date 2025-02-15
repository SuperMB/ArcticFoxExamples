


#> DontProcessFile 
# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 

#> VisualizeAllColumns 

#> ColumnHeaders 



# Example 1
# Get the correlation of all numeric columns in the dataframe
# Seed being used: #> ColumnCorrelation 
# ******************************************************
# ******************************************************

#> Visualize 

#> ColumnCorrelation 

#> print 



# Example 2
# Get the correlation of specific columns in the dataframe
# Seed being used: #> ColumnCorrelation --columns High Low Volume 
# ******************************************************
# ******************************************************

# Focus on the original dataframe, not the correlation dataframe
#> Focus appleStockDf 

#> Visualize 

#> ColumnCorrelation --columns High Low Volume 

#> print 



# Example 3
# Get the correlation of specific columns in the dataframe
# that meet a given condition
# Seed being used: #> ColumnCorrelation --columns High Low Volume --where _High_ > 1.10 * _Open_ 
# ******************************************************
# ******************************************************

#> Focus appleStockDf 

#> Visualize 

#> ColumnCorrelation --columns High Low Volume --where _High_ > 1.10 * _Open_ 

#> print 



