
import pandas as pd
import numpy as np
#> Data pizzerias.csv 
pizzeriasDf = pd.read_csv('pizzerias.csv') 
pizzeriasDf = pd.read_csv('../pizzerias.csv')


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

#Example 1: Get single column
#> ColumnGet Rating 
rating_2 = pizzeriasDf['Rating'] 
rating = pizzeriasDf['Rating']

#Example2: Get multiple columns

#> ColumnGet Location Rating 
#***Analyze rating to learn about: type
#***#> `run script and gather data 
location = pizzeriasDf['Location']
rating_1 = pizzeriasDf['Rating']

