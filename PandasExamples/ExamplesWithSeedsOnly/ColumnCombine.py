
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 


# Setup
# ******************************************************
# ******************************************************

#> Data ModifiedPizzerias.csv 
modifiedPizzeriasDf = pd.read_csv('ModifiedPizzerias.csv') 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

#> ColumnHeaders 
# Pizzeria Name
# Location
# Specialty Pizza
# Price Range
# First Person Rating
# Second Person Rating
# Delivery Options
# Vegan Friendly
# Established Year
# Seating Capacity
# Website 



# Example 1
# ColumnCombine is a bit of a niche seed. The resulting code will
# combine two columns by keeping the value of the first column if
# it is not null / NaN, and if it is, the column will take the
# value of the second column.
#
# In this example, we have two people's ratings in the columns
# First Person Rating and Second Person Rating. However, each
# person did not rate every pizzeria. We will combine the two
# columns to use the First Person Rating when available, and
# otherwise use the Second Person Rating.
#
# Seed being used: #> ColumnCombine First  Person  Rating Second  Person  Rating --keepNonNull 
# ******************************************************
# ******************************************************

#> Visualize --count 20 
print(modifiedPizzeriasDf.head(n=20)) #)1 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  First Person Rating  Second Person Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0              Antonio's Urban          Bronx, NYC         Hawaiian        $$$$                  NaN                   5.0               No             No               NaN              77.0                                NaN
##*** 1            Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$                  NaN                   NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2       Giovanni's Traditional         Queens, NYC              NaN        $$$$                  3.1                   3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN                  NaN                   NaN              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4    Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$                  NaN                   NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
##*** 5       Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $                  4.8                   4.8              Yes             No               NaN              39.0    www.giovanni'straditional57.com
##*** 6               Mario's Garden         Queens, NYC        Pepperoni          $$                  4.1                   NaN               No            Yes               NaN              58.0            www.mario'sgarden62.com
##*** 7    Antonio's Slice of Heaven         Queens, NYC       Margherita           $                  4.0                   4.0              Yes             No            1986.0              21.0   www.antonio'ssliceofheaven82.com
##*** 8      Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $                  3.2                   3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9           Giovanni's Gourmet  Staten Island, NYC              NaN           $                  4.3                   4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com
##*** 10               Mario's Urban                 NaN       Margherita          $$                  4.6                   4.6              Non            Yes            1976.0              42.0             www.mario'surban72.com
##*** 11       Antonio's Traditional         Queens, NYC           Veggie           $                  NaN                   NaN              Non             No            1990.0              22.0     www.antonio'straditional70.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$                  4.6                   NaN              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 13          Giovanni's Gourmet       Brooklyn, NYC       Margherita        $$$$                  4.9                   4.9              Non             No               NaN              97.0        www.giovanni'sgourmet23.com
##*** 14              Mario's Secret          Bronx, NYC           Veggie         $$$                  3.4                   3.4              Yes            Yes            2015.0              35.0            www.mario'ssecret32.com
##*** 15         Luigi's Traditional       Brooklyn, NYC       Margherita         $$$                  4.0                   4.0              Yes            Yes            1961.0              30.0       www.luigi'straditional86.com
##*** 16       Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $                  3.6                   NaN               No             No            1989.0              37.0     www.antonio'straditional57.com
##*** 17          Rosa's Traditional                 NaN              NaN          $$                  NaN                   NaN              Yes            Yes            1959.0              57.0         www.rosa'straditional9.com
##*** 18              Rosa's Gourmet      Manhattan, NYC        Pepperoni         $$$                  4.2                   4.2              Non            Yes            1997.0              49.0            www.rosa'sgourmet31.com
##*** 19             Mario's Gourmet          Bronx, NYC         Hawaiian          $$                  NaN                   NaN              Yes             No            1969.0              75.0                                NaN

#> ColumnCombine First  Person  Rating Second  Person  Rating --keepNonNull 
modifiedPizzeriasDf['First Person Rating'] = modifiedPizzeriasDf['First Person Rating'].combine_first(modifiedPizzeriasDf['Second Person Rating'])
modifiedPizzeriasDf = modifiedPizzeriasDf.drop(columns='Second Person Rating') 

#> ColumnRename --columns First  Person  Rating --to Total  Rating 
modifiedPizzeriasDf = modifiedPizzeriasDf.rename(columns={'First Person Rating': 'Total Rating'}) 

#> Visualize --count 20 
print(modifiedPizzeriasDf.head(n=20)) #)2 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  Total Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0              Antonio's Urban          Bronx, NYC         Hawaiian        $$$$           5.0               No             No               NaN              77.0                                NaN
##*** 1            Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$           NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2       Giovanni's Traditional         Queens, NYC              NaN        $$$$           3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN           NaN              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4    Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$           NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
##*** 5       Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $           4.8              Yes             No               NaN              39.0    www.giovanni'straditional57.com
##*** 6               Mario's Garden         Queens, NYC        Pepperoni          $$           4.1               No            Yes               NaN              58.0            www.mario'sgarden62.com
##*** 7    Antonio's Slice of Heaven         Queens, NYC       Margherita           $           4.0              Yes             No            1986.0              21.0   www.antonio'ssliceofheaven82.com
##*** 8      Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $           3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9           Giovanni's Gourmet  Staten Island, NYC              NaN           $           4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com
##*** 10               Mario's Urban                 NaN       Margherita          $$           4.6              Non            Yes            1976.0              42.0             www.mario'surban72.com
##*** 11       Antonio's Traditional         Queens, NYC           Veggie           $           NaN              Non             No            1990.0              22.0     www.antonio'straditional70.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$           4.6              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 13          Giovanni's Gourmet       Brooklyn, NYC       Margherita        $$$$           4.9              Non             No               NaN              97.0        www.giovanni'sgourmet23.com
##*** 14              Mario's Secret          Bronx, NYC           Veggie         $$$           3.4              Yes            Yes            2015.0              35.0            www.mario'ssecret32.com
##*** 15         Luigi's Traditional       Brooklyn, NYC       Margherita         $$$           4.0              Yes            Yes            1961.0              30.0       www.luigi'straditional86.com
##*** 16       Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $           3.6               No             No            1989.0              37.0     www.antonio'straditional57.com
##*** 17          Rosa's Traditional                 NaN              NaN          $$           NaN              Yes            Yes            1959.0              57.0         www.rosa'straditional9.com
##*** 18              Rosa's Gourmet      Manhattan, NYC        Pepperoni         $$$           4.2              Non            Yes            1997.0              49.0            www.rosa'sgourmet31.com
##*** 19             Mario's Gourmet          Bronx, NYC         Hawaiian          $$           NaN              Yes             No            1969.0              75.0                                NaN


