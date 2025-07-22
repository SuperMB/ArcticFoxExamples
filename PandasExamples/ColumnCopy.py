 
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



# Example 1
# Copy a single column with default new name
# Seed being used: #> ColumnCopy Location 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)1 

##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
#> ColumnCopy Location --exampleTitle Copy a Single Column --example Sometimes, you want to duplicate a column to do computations on the copy, but not modify the original column's content. Passing a column into ColumnCopy will create a copy of the column within the dataframe. By defualt, if no column name is specified, the default column name will be the original column name plus Copy.
pizzeriasDf['LocationCopy'] = pizzeriasDf['Location'] 

#> Visualize 
print(pizzeriasDf.head()) #)2 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website        LocationCopy
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN          Bronx, NYC
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com  Staten Island, NYC
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com         Queens, NYC
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com                 NaN
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com  Staten Island, NYC



# Example 2
# Copy a column and specify the new name
# Seed being used: #> ColumnCopy Specialty  Pizza --to Old  Specialty  Pizza 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)3 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website        LocationCopy
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN          Bronx, NYC
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com  Staten Island, NYC
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com         Queens, NYC
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com                 NaN
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com  Staten Island, NYC

#> ColumnCopy Specialty  Pizza --to Old  Specialty  Pizza --exampleTitle Copy a Column and Specify the New Column Name --example Similar to the previous example, except this time we specify the new column's name with the --to option. 
pizzeriasDf['Old Specialty Pizza'] = pizzeriasDf['Specialty Pizza'] 

#> Visualize 
print(pizzeriasDf.head()) #)4 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website        LocationCopy Old Specialty Pizza
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN          Bronx, NYC            Hawaiian
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com  Staten Island, NYC            Hawaiian
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com         Queens, NYC                 NaN
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com                 NaN            Hawaiian
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com  Staten Island, NYC     Buffalo Chicken



# Example 3
# Copy multiple columns and specify the new names
# Seed being used: #> ColumnCopy Rating Website --to PreviousRating PreviousWebsite 
# ******************************************************
# ******************************************************

#> Visualize 
print(pizzeriasDf.head()) #)5 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website        LocationCopy Old Specialty Pizza
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN          Bronx, NYC            Hawaiian
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com  Staten Island, NYC            Hawaiian
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com         Queens, NYC                 NaN
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com                 NaN            Hawaiian
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com  Staten Island, NYC     Buffalo Chicken

#> ColumnCopy Rating Website --to PreviousRating PreviousWebsite --exampleTitle Copying Multiple Columns --example To copy multiple columns, instead of just one, add multiple column names to the kit. In this case, we also supplied multiple new column names with the --to option.  
pizzeriasDf['PreviousRating'] = pizzeriasDf['Rating']
pizzeriasDf['PreviousWebsite'] = pizzeriasDf['Website'] 

#> Visualize 
print(pizzeriasDf.head()) #)6 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website        LocationCopy Old Specialty Pizza  PreviousRating                    PreviousWebsite
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN          Bronx, NYC            Hawaiian             5.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com  Staten Island, NYC            Hawaiian             NaN         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com         Queens, NYC                 NaN             3.1    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com                 NaN            Hawaiian             3.1  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com  Staten Island, NYC     Buffalo Chicken             NaN   www.antonio'ssliceofheaven22.com
