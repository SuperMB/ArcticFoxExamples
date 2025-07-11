 
import pandas as pd
import numpy as np
import arcticFoxDataframesEqual  
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
# Compare two dataframes to see if their content is identical
# Use defaults to compare the most recent two dataframes
# Seed being used: #> DataframesEqual 
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

#> DataframesEqual 
dataframesEqual = pizzeriasDf.equals()
#ISSUE: Could not find a target automation, Dataframe, Data automation(s), or a variable assignment 

#> print 
print(dataframesEqual) #)2 
##*** True



# Example 2
# Compare two dataframes to see if their content is identical
# However, this time they do not have equal contents
# Seed being used: #> DataframesEqual 
# ******************************************************
# ******************************************************

# Focus on the original dataframe
#> Focus pizzeriasDf 
# Setting focus to pizzeriasDf 

#> Visualize 
print(pizzeriasDf.head()) #)3 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating Delivery Options Vegan Friendly  Established Year  Seating Capacity                            Website
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0               No             No               NaN              77.0                                NaN
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN              Yes            Yes               NaN              35.0         www.giovanni'ssecret94.com
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1              Yes            Yes               NaN               NaN    www.giovanni'straditional33.com
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1              Non             No            1991.0              11.0  www.giovanni'ssliceofheaven16.com
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN               No             No            1989.0              23.0   www.antonio'ssliceofheaven22.com

#> ColumnRemove 5 --throughLastColumn 
pizzeriasDf.drop(columns=pizzeriasDf.columns[5:], axis=1, inplace=True) 

#> Visualize 
print(pizzeriasDf.head()) #)4 
##***                 Pizzeria Name            Location  Specialty Pizza Price Range  Rating
##*** 0             Antonio's Urban          Bronx, NYC         Hawaiian        $$$$     5.0
##*** 1           Giovanni's Secret  Staten Island, NYC         Hawaiian         $$$     NaN
##*** 2      Giovanni's Traditional         Queens, NYC              NaN        $$$$     3.1
##*** 3  Giovanni's Slice of Heaven                 NaN         Hawaiian         NaN     3.1
##*** 4   Antonio's Slice of Heaven  Staten Island, NYC  Buffalo Chicken          $$     NaN

#> DataframesEqual 
#***run script to analyze variables - need to analyze dataframesEqual for type 

#> print 
print(dataframesEqual) #)5 
##*** False


 
arcticFoxDataframesEqual.analyzeVariables([ (value, eval(value)) for value in arcticFoxDataframesEqual.variables(dir() + [] )] ) 