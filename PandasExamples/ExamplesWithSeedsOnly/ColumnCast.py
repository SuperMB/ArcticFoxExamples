
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data Pizzerias.csv 
pizzeriasDf = pd.read_csv('Pizzerias.csv') 

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

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 



# NOTE
# ******************************************************
# ******************************************************
# Casting a column in pandas informs pandas on how to interpret the column,
# Casting will not work for data that does not conform to the specified cast.
# For example, you cannot cast a column of street addresses, such as:
# 138 Harp Dr.
# to and integer and expect pandas to select the numeric portion of the address.
# Instead, pandas will throw an error stating that it cannot convert the column
# to integers.
#
#
# Also, casting rows with NaN's may be an issue. If this appears, use
# RowRemow to remove rows with missing data, or CleanData to fill in missing
# data values.
# ******************************************************
# ******************************************************



# Example 1
# Casting a column to integer
# Seed being used: #> ColumnCast Rating --type int 
# ******************************************************
# ******************************************************

#> RowRemove --missing 
pizzeriasDf = pizzeriasDf.dropna() 

#> Visualize 
print(pizzeriasDf.head()) #)1 

##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $     4.0              Yes             No            1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$     3.4              Yes            Yes            2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$     4.0              Yes            Yes            1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $     3.6               No             No            1989.0              37.0    www.antonio'straditional57.com
#> ColumnCast Rating --type int 
pizzeriasDf['Rating'] = pizzeriasDf['Rating'].astype('int') 

#> Visualize 
print(pizzeriasDf.head()) #)2 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $       4              Yes             No            1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$       4              Non             No            1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$       3              Yes            Yes            2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$       4              Yes            Yes            1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $       3               No             No            1989.0              37.0    www.antonio'straditional57.com



# Example 2
# Casting multiple columns to string
# Seed being used: #> ColumnCast Speciality  Pizza Established  Year --type string 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)3 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $       4              Yes             No            1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$       4              Non             No            1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$       3              Yes            Yes            2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$       4              Yes            Yes            1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $       3               No             No            1989.0              37.0    www.antonio'straditional57.com

#> ColumnCast Specialty  Pizza Established  Year --type string 
pizzeriasDf['Specialty Pizza'] = pizzeriasDf['Specialty Pizza'].astype('str')
pizzeriasDf['Established Year'] = pizzeriasDf['Established Year'].astype('str') 

#> Visualize 
print(pizzeriasDf.head()) #)4 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $       4              Yes             No           1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$       4              Non             No           1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$       3              Yes            Yes           2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$       4              Yes            Yes           1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $       3               No             No           1989.0              37.0    www.antonio'straditional57.com



# Example 3
# Casting a column to float
# Seed being used: #> ColumnCast Seating  Capacity --type float 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)5 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $       4              Yes             No           1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$       4              Non             No           1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$       3              Yes            Yes           2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$       4              Yes            Yes           1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $       3               No             No           1989.0              37.0    www.antonio'straditional57.com

#> ColumnCast Seating  Capacity --type float 
pizzeriasDf['Seating Capacity'] = pizzeriasDf['Seating Capacity'].astype('float') 

#> Visualize 
print(pizzeriasDf.head()) #)6 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $       4              Yes             No           1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$       4              Non             No           1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$       3              Yes            Yes           2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$       4              Yes            Yes           1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $       3               No             No           1989.0              37.0    www.antonio'straditional57.com
