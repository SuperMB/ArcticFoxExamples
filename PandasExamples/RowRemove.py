 
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
# Remove rows with missing values from any column
# Seed being used: #> RowRemove --missing 
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

#> RowRemove --missing --exampleTitle Remove Rows with Empty Cells --example Data is often not clean and there might be rows within a dataframe that are missing values from one or more columns. To simply remove all rows with missing cells, use the RowRemove kit with the missing option. 
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
# Remove rows with missing values in specified columns
# Seed being used: #> RowRemove --missing --columns Rating Established  Year 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> RowRemove --missing --columns Rating Established  Year --exampleTitle Remove Rows with Missing Cells in Specified Columns --example Rather than removing rows with any missing cells, sometimes we only want to clean up a dataframe that is missing values in specific columns. In this example, we only remove rows that have missing values in the Rating or Established Year columns.
pizzeriasDf = pizzeriasDf.dropna(subset = ['Rating', 'Established Year']).reset_index(drop=True) 

#> Visualize --count 10 
print(pizzeriasDf.head(n=10)) #)4 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 7    Antonio's Slice of Heaven         Queens, NYC       Margherita           $     4.0              Yes             No            1986.0              21.0   www.antonio'ssliceofheaven82.com
##*** 8      Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $     3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9           Giovanni's Gourmet  Staten Island, NYC              NaN           $     4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com
##*** 10               Mario's Urban                 NaN       Margherita          $$     4.6              Non            Yes            1976.0              42.0             www.mario'surban72.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 14              Mario's Secret          Bronx, NYC           Veggie         $$$     3.4              Yes            Yes            2015.0              35.0            www.mario'ssecret32.com
##*** 15         Luigi's Traditional       Brooklyn, NYC       Margherita         $$$     4.0              Yes            Yes            1961.0              30.0       www.luigi'straditional86.com
##*** 16       Antonio's Traditional          Bronx, NYC  Buffalo Chicken           $     3.6               No             No            1989.0              37.0     www.antonio'straditional57.com
##*** 17          Rosa's Traditional                 NaN              NaN          $$     4.6              Yes            Yes            1959.0              57.0         www.rosa'straditional9.com



# Example 3
# Remove rows at an index
# Seed being used: #> RowRemove --index 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
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

#> RowRemove --index 3 --exampleTitle Remove Row at Index --example When you have specific rows that you want to remove, you can remove them from the dataframe by specifying the row's index with the index option. 
pizzeriasDf = pizzeriasDf.drop(3).reset_index(drop=True) 

#> Visualize 
print(pizzeriasDf.head()) #)6 
##***                Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                           Website
##*** 0            Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                               NaN
##*** 1          Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0        www.giovanni'ssecret94.com
##*** 2     Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN   www.giovanni'straditional33.com
##*** 4  Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0  www.antonio'ssliceofheaven22.com
##*** 5     Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $     4.8              Yes             No               NaN              39.0   www.giovanni'straditional57.com



# Example 4
# Remove rows after an index
# Seed being used: #> RowRemove --indexStart 3 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize 
print(pizzeriasDf.head()) #)7 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowRemove --indexStart 3 --exampleTitle Remove All Rows Starting At an Index --example Rather than remove a single row from the dataframe, sometimes you want to remove many, many more rows. Using the indexStart option, without the indexStop option, will remove the row at the specified index and all rows after it. In this example, the row at index 3 through the end of the dataframe are removed. 
pizzeriasDf = pizzeriasDf.drop(pizzeriasDf.index[3:]) 

#> Visualize --count 10 
print(pizzeriasDf.head(n=10)) #)8 
##***             Pizzeria Name            Location Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                          Website
##*** 0         Antonio's Urban          Bronx, NYC        Hawaiian        $$$$     5.0               No             No               NaN              77.0                              NaN
##*** 1       Giovanni's Secret  Staten Island, NYC        Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0       www.giovanni'ssecret94.com
##*** 2  Giovanni's Traditional         Queens, NYC             NaN        $$$$     3.1              Yes            Yes               NaN               NaN  www.giovanni'straditional33.com



# Example 5
# Remove rows before an index
# Seed being used: #> RowRemove --indexStop 50 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize 
print(pizzeriasDf.head()) #)9 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowRemove --indexStop 50 --exampleTitle Remove All Rows Up To an Index --example The previous example removed rows at and after an index. This time, we remove all rows starting at the first row up to, and including, the specified row index. In this example, we rows from the start of the dataframe up to and including the row at index 50. This is done when you use the indexStop option without the indexStart option.
pizzeriasDf = pizzeriasDf.drop(pizzeriasDf.index[:50+1]).reset_index(drop=True) 

#> Visualize 
print(pizzeriasDf.head()) #)10 
##***           Pizzeria Name        Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                     Website
##*** 51        Luigi's Urban             NaN              NaN         $$$     3.9              Non            Yes            1982.0               NaN       www.luigi'surban6.com
##*** 52       Mario's Secret      Bronx, NYC       Margherita         NaN     3.3              Yes             No               NaN              28.0     www.mario'ssecret73.com
##*** 53      Mario's Gourmet             NaN       Margherita           $     3.0               No            Yes               NaN              15.0    www.mario'sgourmet84.com
##*** 54  Luigi's Traditional             NaN  Buffalo Chicken           $     4.1              Yes            Yes            1969.0              93.0                         NaN
##*** 55    Antonio's Gourmet  Manhattan, NYC           Veggie        $$$$     4.1              Yes            Non            1967.0              36.0  www.antonio'sgourmet38.com



# Example 6
# Remove rows within a range
# Seed being used: #> RowRemove --indexStart 5 --indexStop 10 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize 
print(pizzeriasDf.head()) #)11 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> RowRemove --indexStart 5 --indexStop 10 --exampleTitle Remove All Rows Starting at an Index to a Second Index --example Combining the previous two examples, this time we use both the indexStart and indexStop options. This will remove only rows from the row at the indexStart index to the indexStop index. It will be inclusive of both indexes. Therefore, this example will remove rows from and including the row at index 5 to the row at index 10. 
pizzeriasDf = pizzeriasDf.drop(pizzeriasDf.index[5:10+1]).reset_index(drop=True) 

#> Visualize --count 10 
print(pizzeriasDf.head(n=10)) #)12 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0              Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1            Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2       Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4    Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
##*** 11       Antonio's Traditional         Queens, NYC           Veggie           $     NaN              Non             No            1990.0              22.0     www.antonio'straditional70.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 13          Giovanni's Gourmet       Brooklyn, NYC       Margherita        $$$$     4.9              Non             No               NaN              97.0        www.giovanni'sgourmet23.com
##*** 14              Mario's Secret          Bronx, NYC           Veggie         $$$     3.4              Yes            Yes            2015.0              35.0            www.mario'ssecret32.com
##*** 15         Luigi's Traditional       Brooklyn, NYC       Margherita         $$$     4.0              Yes            Yes            1961.0              30.0       www.luigi'straditional86.com



# Example 7
# Remove rows that meet a criteria
# Seed being used: #> RowRemove --where _Pizzeria  Name_ contains Antonio 
# ******************************************************
# ******************************************************

# Reset original dataframe
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> Visualize --count 10 
print(pizzeriasDf.head(n=10)) #)13 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com
##*** 5      Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $     4.8              Yes             No               NaN              39.0    www.giovanni'straditional57.com
##*** 6              Mario's Garden         Queens, NYC        Pepperoni          $$     4.1               No            Yes               NaN              58.0            www.mario'sgarden62.com
##*** 7   Antonio's Slice of Heaven         Queens, NYC       Margherita           $     4.0              Yes             No            1986.0              21.0   www.antonio'ssliceofheaven82.com
##*** 8     Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $     3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9          Giovanni's Gourmet  Staten Island, NYC              NaN           $     4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com

#> RowRemove --where _Pizzeria  Name_ contains Antonio --exampleTitle Remove Rows That Match a Criteria --example Rather than specifying certain rows indexes, or rows with missing data, other times you want to remove rows that fit into a specified criteria. In this example, we remove all rows where the Pizzeria Name contains the word Antonio.  
pizzeriasDf = pizzeriasDf[~(pizzeriasDf['Pizzeria Name'].astype('str').str.contains('Antonio').fillna(False))].reset_index(drop=True) 

#> Visualize --count 10 
print(pizzeriasDf.head(n=10)) #)14 
##***                  Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 1            Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2       Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3   Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 5       Giovanni's Traditional       Brooklyn, NYC  Buffalo Chicken           $     4.8              Yes             No               NaN              39.0    www.giovanni'straditional57.com
##*** 6               Mario's Garden         Queens, NYC        Pepperoni          $$     4.1               No            Yes               NaN              58.0            www.mario'sgarden62.com
##*** 8      Luigi's Slice of Heaven         Queens, NYC         Hawaiian           $     3.2              Yes            Yes            1971.0              99.0                                NaN
##*** 9           Giovanni's Gourmet  Staten Island, NYC              NaN           $     4.3              Non            Yes            2006.0              53.0        www.giovanni'sgourmet90.com
##*** 10               Mario's Urban                 NaN       Margherita          $$     4.6              Non            Yes            1976.0              42.0             www.mario'surban72.com
##*** 12      Giovanni's Traditional  Staten Island, NYC  Buffalo Chicken          $$     4.6              Non             No            1983.0              87.0    www.giovanni'straditional30.com
##*** 13          Giovanni's Gourmet       Brooklyn, NYC       Margherita        $$$$     4.9              Non             No               NaN              97.0        www.giovanni'sgourmet23.com

