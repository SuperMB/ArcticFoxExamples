 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 



# Setup
# ******************************************************
# ******************************************************

#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> ColumnHeaders 
# Pizzeria Name
# Location
# Specialty Pizza
# Price Range
# Rating
# Delivery Options
# Vegan Friendly
# Established Year
# Seating Capacity
# Website 



# Example 1
# Get the total number of rows and print the result into the file
# Seed being used: #> RowCount --print 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)1 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowCount --print --exampleTitle Count Total Number of Rows --example One of the simplest checks you can make is to count how many rows are in a dataframe. This is useful to verify that the data loaded correctly or to understand the dataset size before applying transformations.
pizzeriasDfRowCount = pizzeriasDf.shape[0]
print(pizzeriasDfRowCount) #)2 
##*** 1000



# Example 2
# Count the number of rows with missing values
# Seed being used: #> RowCount --missing 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)3 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowCount --missing --exampleTitle Count Rows with Missing Values --example This example counts how many rows contain missing values in any column. It’s a useful first step when deciding whether to clean, impute, or drop incomplete records.
pizzeriasDfMissingRowCount = pizzeriasDf.isnull().any(axis=1).sum() 

#> print 
print(pizzeriasDfMissingRowCount) #)4 
##*** 663



# Example 3
# Count the number of rows WITHOUT missing values
# Seed being used: #> RowCount --notMissing 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)5 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowCount --notMissing --exampleTitle Count Rows with No Missing Values --example In contrast to counting rows with missing data, this counts only those rows that are fully populated. It helps you isolate the clean records in your dataset.
pizzeriasDfNotMissingRowCount = pizzeriasDf.shape[0] - pizzeriasDf.isnull().any(axis=1).sum() 

#> print 
print(pizzeriasDfNotMissingRowCount) #)6 
##*** 337



# Example 4
# Count the number of rows where a specified value occurs
# Seed being used: #> RowCount --values 3.0 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)7 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowCount --values 3.0 --exampleTitle Count Rows Containing a Specific Value --example This example checks how many rows contain the exact value 3.0 in any column. This can be useful when searching for numeric markers or flags across a dataframe.
pizzeriasDfRowCount_1 = (pizzeriasDf.isin([3.0]).any(axis=1).sum()) 

#> print 
print(pizzeriasDfRowCount_1) #)8 
##*** 20



# Example 5
# Count the number of rows that meet a criteria
# Seed being used: #> RowCount --where _Specialty  Pizza_ == Hawaiian and _Rating_ < 3.5 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)9 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowCount --where _Specialty  Pizza_ == Hawaiian and _Rating_ < 3.5 --exampleTitle Count Rows That Match a Condition --example Sometimes you want to count how many rows meet a specific set of criteria. This example counts rows where the Specialty Pizza is Hawaiian and the Rating is less than 3.5.
pizzeriasDfRowCount_2 = pizzeriasDf[(pizzeriasDf['Specialty Pizza'] == 'Hawaiian') & (pizzeriasDf['Rating'] < 3.5)].shape[0] 

#> print 
print(pizzeriasDfRowCount_2) #)10 
##*** 35

