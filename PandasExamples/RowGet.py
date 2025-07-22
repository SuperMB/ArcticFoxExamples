 
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
# Get the row at an index
# Seed being used: #> RowGet --index 10 
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

#> RowGet --index 10 --exampleTitle Get a Row at an Index --example When you want to get rows at soecified indexes, you can use RowGet with the index option to get the rows at the specified indexes. Here, we get the row at index 10. 
pizzeriasDfRow10 = pizzeriasDf.iloc[10] 

#> print 
print(pizzeriasDfRow10) #)2 
##*** Pizzeria Name                Mario's Urban
##*** Location                               NaN
##*** Specialty Pizza                 Margherita
##*** Price Range                             $$
##*** Rating                                 4.6
##*** Delivery Options                       Non
##*** Vegan Friendly                         Yes
##*** Established Year                    1976.0
##*** Seating Capacity                      42.0
##*** Website             www.mario'surban72.com
##*** Name: 10, dtype: object



# Example 2
# Get rows within a range
# Seed being used: #> RowGet --indexStart 20 --indexStop 30 
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

#> RowGet --indexStart 20 --indexStop 30 --exampleTitle Get Rows From One Index Up To a Second Index --example Rather then only getting rows at only specified indexes, 
pizzeriasDfRowsFrom20To30 = pizzeriasDf.iloc[20:30] 

#> print 
print(pizzeriasDfRowsFrom20To30) #)4 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 20             Luigi's Secret       Brooklyn, NYC       Margherita          $$     4.6               No             No               NaN              82.0            www.luigi'ssecret9.com
##*** 21            Luigi's Gourmet  Staten Island, NYC       Margherita           $     3.8              Yes             No            2009.0              96.0          www.luigi'sgourmet13.com
##*** 22        Mario's Traditional          Bronx, NYC              NaN         $$$     4.8              Yes            Yes               NaN              88.0                               NaN
##*** 23           Antonio's Secret                 NaN  Buffalo Chicken           $     4.1              Yes            Yes            2014.0              86.0          www.antonio'ssecret3.com
##*** 24             Luigi's Secret      Manhattan, NYC       Margherita           $     3.3               No            Non            2000.0               NaN           www.luigi'ssecret35.com
##*** 25             Rosa's Gourmet                 NaN  Buffalo Chicken         $$$     4.4              Yes            Yes            1985.0              90.0                               NaN
##*** 26           Giovanni's Urban         Queens, NYC       Margherita         $$$     4.6              Yes            Yes            1973.0              57.0         www.giovanni'surban21.com
##*** 27          Antonio's Gourmet       Brooklyn, NYC        Pepperoni        $$$$     3.6               No             No            1976.0              11.0        www.antonio'sgourmet64.com
##*** 28               Rosa's Urban          Bronx, NYC         Hawaiian         NaN     4.7               No            Non            1951.0              93.0                               NaN
##*** 29  Antonio's Slice of Heaven          Bronx, NYC       Margherita          $$     4.8              Yes            Yes            1980.0              29.0  www.antonio'ssliceofheaven52.com



# Example 3
# Get rows after an index
# Seed being used: #> RowGet --indexStart 200 
# ******************************************************
# ******************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 
# Setting focus to pizzeriasDf 

#> Visualize 
print(pizzeriasDf.head()) #)5 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowGet --indexStart 200 --example 
pizzeriasDfRowsStartingAt200 = pizzeriasDf.iloc[200:] 

#> print 
print(pizzeriasDfRowsStartingAt200) #)6 
##***                  Pizzeria Name        Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 200         Rosa's Traditional   Brooklyn, NYC        Pepperoni          $$     4.3              Yes             No            1966.0              53.0                               NaN
##*** 201             Luigi's Garden             NaN         Hawaiian         $$$     3.1              Yes             No               NaN              62.0           www.luigi'sgarden90.com
##*** 202          Giovanni's Secret  Manhattan, NYC           Veggie          $$     3.5               No            Non            1979.0              19.0        www.giovanni'ssecret21.com
##*** 203         Rosa's Traditional  Manhattan, NYC       Margherita         $$$     3.7              Yes            Non            1994.0              96.0                               NaN
##*** 204            Luigi's Gourmet             NaN           Veggie          $$     3.9              Yes            Yes            2000.0              61.0           www.luigi'sgourmet9.com
##*** ..                         ...             ...              ...         ...     ...              ...            ...               ...               ...                               ...
##*** 995           Antonio's Secret   Brooklyn, NYC       Margherita          $$     3.5              Non             No            1975.0              96.0                               NaN
##*** 996    Luigi's Slice of Heaven  Manhattan, NYC  Buffalo Chicken         $$$     4.2              Yes             No            1994.0               NaN    www.luigi'ssliceofheaven86.com
##*** 997  Antonio's Slice of Heaven  Manhattan, NYC       Margherita           $     4.7              Yes             No            2012.0              85.0  www.antonio'ssliceofheaven89.com
##*** 998               Rosa's Urban      Bronx, NYC  Buffalo Chicken           $     4.9               No             No            2016.0              31.0             www.rosa'surban61.com
##*** 999            Mario's Gourmet     Queens, NYC           Veggie        $$$$     3.2              Yes             No            2001.0              46.0          www.mario'sgourmet18.com
##***
##*** [800 rows x 10 columns]



# Example 4
# Get rows before an index
# Seed being used: #> RowGet --indexStop 30 
# ******************************************************
# *****************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 
# Setting focus to pizzeriasDf 

#> Visualize 
print(pizzeriasDf.head()) #)7 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowGet --indexStop 30 --example 
pizzeriasDfRowsStoppingAt30 = pizzeriasDf.iloc[:30] 

#> print 
print(pizzeriasDfRowsStoppingAt30) #)8 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0              Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1            Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2       Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4    Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
##*** 5       Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $     4.8              Yes             No               NaN              39.0    www.giovanni'straditional57.com
##*** 6               Mario's Garden         Queens, NYC        Pepperoni          $$     4.1               No            Yes               NaN              58.0            www.mario'sgarden62.com
##*** 7    Antonio's Slice of Heaven         Queens, NYC       Margherita           $     4.0              Yes             No            1986.0              21.0   www.antonio'ssliceofheaven82.com
##*** 8      Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $     3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9           Giovanni's Gourmet  Staten Island, NYC              NaN           $     4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com
##*** 10               Mario's Urban                 NaN       Margherita          $$     4.6              Non            Yes            1976.0              42.0             www.mario'surban72.com
##*** 11       Antonio's Traditional         Queens, NYC           Veggie           $     NaN              Non             No            1990.0              22.0     www.antonio'straditional70.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 13          Giovanni's Gourmet       Brooklyn, NYC       Margherita        $$$$     4.9              Non             No               NaN              97.0        www.giovanni'sgourmet23.com
##*** 14              Mario's Secret          Bronx, NYC           Veggie         $$$     3.4              Yes            Yes            2015.0              35.0            www.mario'ssecret32.com
##*** 15         Luigi's Traditional       Brooklyn, NYC       Margherita         $$$     4.0              Yes            Yes            1961.0              30.0       www.luigi'straditional86.com
##*** 16       Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $     3.6               No             No            1989.0              37.0     www.antonio'straditional57.com
##*** 17          Rosa's Traditional                 NaN              NaN          $$     4.6              Yes            Yes            1959.0              57.0         www.rosa'straditional9.com
##*** 18              Rosa's Gourmet      Manhattan, NYC        Pepperoni         $$$     4.2              Non            Yes            1997.0              49.0            www.rosa'sgourmet31.com
##*** 19             Mario's Gourmet          Bronx, NYC         Hawaiian          $$     NaN              Yes             No            1969.0              75.0                                NaN
##*** 20              Luigi's Secret       Brooklyn, NYC       Margherita          $$     4.6               No             No               NaN              82.0             www.luigi'ssecret9.com
##*** 21             Luigi's Gourmet  Staten Island, NYC       Margherita           $     3.8              Yes             No            2009.0              96.0           www.luigi'sgourmet13.com
##*** 22         Mario's Traditional          Bronx, NYC              NaN         $$$     4.8              Yes            Yes               NaN              88.0                                NaN
##*** 23            Antonio's Secret                 NaN  Buffalo Chicken           $     4.1              Yes            Yes            2014.0              86.0           www.antonio'ssecret3.com
##*** 24              Luigi's Secret      Manhattan, NYC       Margherita           $     3.3               No            Non            2000.0               NaN            www.luigi'ssecret35.com
##*** 25              Rosa's Gourmet                 NaN  Buffalo Chicken         $$$     4.4              Yes            Yes            1985.0              90.0                                NaN
##*** 26            Giovanni's Urban         Queens, NYC       Margherita         $$$     4.6              Yes            Yes            1973.0              57.0          www.giovanni'surban21.com
##*** 27           Antonio's Gourmet       Brooklyn, NYC        Pepperoni        $$$$     3.6               No             No            1976.0              11.0         www.antonio'sgourmet64.com
##*** 28                Rosa's Urban          Bronx, NYC         Hawaiian         NaN     4.7               No            Non            1951.0              93.0                                NaN
##*** 29   Antonio's Slice of Heaven          Bronx, NYC       Margherita          $$     4.8              Yes            Yes            1980.0              29.0   www.antonio'ssliceofheaven52.com



# Example 5
# Get rows that meet a criteria
# Seed being used: #> RowGet --where _Location_ contains Queens 
# ******************************************************
# *****************************************************

# Reset focus to original dataframe
#> Focus pizzeriasDf 
# Setting focus to pizzeriasDf 

#> Visualize 
print(pizzeriasDf.head()) #)9 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowGet --where _Location_ contains Queens --example 
pizzeriasDf = pizzeriasDf[pizzeriasDf['Location'].astype('str').str.contains('Queens').fillna(False)] 

#> print 
print(pizzeriasDf) #)10 
##***                  Pizzeria Name     Location Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 2       Giovanni's Traditional  Queens, NYC             NaN        $$$$     3.1              Yes            Yes               NaN               NaN   www.giovanni'straditional33.com
##*** 6               Mario's Garden  Queens, NYC       Pepperoni          $$     4.1               No            Yes               NaN              58.0           www.mario'sgarden62.com
##*** 7    Antonio's Slice of Heaven  Queens, NYC      Margherita           $     4.0              Yes             No            1986.0              21.0  www.antonio'ssliceofheaven82.com
##*** 8      Luigi's Slice of Heaven  Queens, NYC        Hawaiian           $     3.2              Yes            Yes            1971.0              99.0                               NaN
##*** 11       Antonio's Traditional  Queens, NYC          Veggie           $     NaN              Non             No            1990.0              22.0    www.antonio'straditional70.com
##*** ..                         ...          ...             ...         ...     ...              ...            ...               ...               ...                               ...
##*** 958             Luigi's Secret  Queens, NYC        Hawaiian        $$$$     NaN              Non            Yes            1991.0              82.0            www.luigi'ssecret9.com
##*** 964            Luigi's Gourmet  Queens, NYC        Hawaiian        $$$$     3.2              Yes            Yes            2012.0              58.0          www.luigi'sgourmet85.com
##*** 978              Mario's Urban  Queens, NYC       Pepperoni         $$$     4.2              Yes             No            2011.0              82.0            www.mario'surban50.com
##*** 984          Giovanni's Garden  Queens, NYC       Pepperoni          $$     4.2              Yes             No            2007.0              61.0        www.giovanni'sgarden42.com
##*** 999            Mario's Gourmet  Queens, NYC          Veggie        $$$$     3.2              Yes             No            2001.0              46.0          www.mario'sgourmet18.com
##***
##*** [159 rows x 10 columns]
