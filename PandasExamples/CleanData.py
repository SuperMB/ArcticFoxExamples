 
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
# Removing missing data from the dataframe
# Seed being used: #> CleanData --removeMissing 
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

#> CleanData --removeMissing  Remove Rows with Missing Cells --example One of the easiest ways to clean a dataframe with missing cells is to remove the rows with missing cells entirely. Using CleanData and passing in the option --removeMissing will write code to remove rows with missing cells. 
pizzeriasDf = pizzeriasDf.dropna().reset_index(drop=True) 

#> Visualize 
print(pizzeriasDf.head()) #)2 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $     4.0              Yes             No            1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 12     Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0   www.giovanni'straditional30.com
##*** 14             Mario's Secret          Bronx, NYC           Veggie         $$$     3.4              Yes            Yes            2015.0              35.0           www.mario'ssecret32.com
##*** 15        Luigi's Traditional       Brooklyn, NYC       Margherita         $$$     4.0              Yes            Yes            1961.0              30.0      www.luigi'straditional86.com
##*** 16      Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $     3.6               No             No            1989.0              37.0    www.antonio'straditional57.com



# Example 2
# Fill missing Rating values with mean of the column
# Seed being used: #> CleanData --fill --columns Rating --mean 
# ******************************************************
# ******************************************************

# Reload the data since the last example removed the missing value
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize 
print(pizzeriasDf.head()) #)3 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> CleanData --fill --columns Rating --mean --exampleTitle Fill Missing Cells with Mean --example Rather than removing missing cells from a dataframe, it may be beneficial to keep those rows and fill the missing cells with a statistical value. In this case, we fill the missing cells with the mean of the colum. 
pizzeriasDf[ ['Rating'] ] = pizzeriasDf[ ['Rating'] ].apply(lambda col: col.fillna(col.mean())) 

#> Visualize 
print(pizzeriasDf.head()) #)4 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range    Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$  5.000000               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$  4.011452              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$  3.100000              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN  3.100000              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$  4.011452               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com



# Example 3
# Interpolate missing Rating values using the nearest non-NaN values
# Seed being used: #> CleanData --interpolate --columns Rating 
# ******************************************************
# ******************************************************

# Reload the data since the last example filled in missing values with the mean
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize 
print(pizzeriasDf.head()) #)5 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> CleanData --interpolate --columns Rating --exampleTitle Interpolate Missing Cells --example Another approach to cleaning a data set with missing cells is to fill the cells with a midpoint value based on the surrounding cells. This process is known as interpoloation. Rather than being replace with a statistical value, each cell will receive an interpolated value based on the cells arround it. 
pizzeriasDf[['Rating']] = pizzeriasDf[['Rating']].interpolate() 

#> Visualize 
print(pizzeriasDf.head()) #)6 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$    5.00               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$    4.05              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$    3.10              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN    3.10              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$    3.95               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

