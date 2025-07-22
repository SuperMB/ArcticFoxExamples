 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 




# Setup
# ******************************************************
# ******************************************************

#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 

#> VisualizeAllColumns 
# Code added to start of file to display all columns for dataframes 

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
# Get a single column
# Seed being used: #> ColumnGet Rating 
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

#> ColumnGet Rating --exampleTitle Get a Single Column --example Sometimes you only want to look at a single column within a dataframe. This example shows how to extract the values of the Rating column on its own, allowing you to work with it independently of the rest of the dataset.
rating = pizzeriasDf['Rating'] 

#> print 
print(rating) #)2 
##*** 0      5.0
##*** 1      NaN
##*** 2      3.1
##*** 3      3.1
##*** 4      NaN
##***       ...
##*** 995    3.5
##*** 996    4.2
##*** 997    4.7
##*** 998    4.9
##*** 999    3.2
##*** Name: Rating, Length: 1000, dtype: float64



# Example 2
# Get multiple columns
# Seed being used: #> ColumnGet Location Specialty  Pizza 
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

#> ColumnGet Location Specialty  Pizza --exampleTitle Get Multiple Columns --example You may want to pull out specific columns from the dataframe to examine or work with side-by-side. This example extracts the Location and Specialty Pizza columns so that we can focus only on those fields and ignore the others.
location = pizzeriasDf['Location']
specialtyPizza = pizzeriasDf['Specialty Pizza'] 

#> print location 
print(location) #)4 
##*** 0              Bronx, NYC
##*** 1      Staten Island, NYC
##*** 2             Queens, NYC
##*** 3                     NaN
##*** 4      Staten Island, NYC
##***               ...
##*** 995         Brooklyn, NYC
##*** 996        Manhattan, NYC
##*** 997        Manhattan, NYC
##*** 998            Bronx, NYC
##*** 999           Queens, NYC
##*** Name: Location, Length: 1000, dtype: object

#> print specialtyPizza 
print(specialtyPizza) #)5 
##*** 0             Hawaiian
##*** 1             Hawaiian
##*** 2                  NaN
##*** 3             Hawaiian
##*** 4      Buffalo Chicken
##***             ...
##*** 995         Margherita
##*** 996    Buffalo Chicken
##*** 997         Margherita
##*** 998    Buffalo Chicken
##*** 999             Veggie
##*** Name: Specialty Pizza, Length: 1000, dtype: object
