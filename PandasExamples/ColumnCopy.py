
import pandas as pd
import numpy as np

#> Data Pizzerias.csv 
pizzeriasDf = pd.read_csv('Pizzerias.csv') 
pizzeriasDf = pd.read_csv('../Pizzerias.csv')

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

#Example 1: Copy single column
#> ColumnCopy Location --to new_location 
pizzeriasDf['new_location'] = pizzeriasDf['Location'] 
pizzeriasDf['new_location'] = pizzeriasDf['Location']

#Example 2: Copy multiple columns
#> ColumnCopy Rating Website --to newRating newWebsite 
pizzeriasDf['newRating'] = pizzeriasDf['Rating']
pizzeriasDf['newWebsite'] = pizzeriasDf['Website'] 
pizzeriasDf['newRating'] = pizzeriasDf['Rating']
pizzeriasDf['newWebsite'] = pizzeriasDf['Website']

#> print 
print(pizzeriasDf) #)1 
print(pizzeriasDf) ##1
