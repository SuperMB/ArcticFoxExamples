#>1
import pandas as pd
import numpy as np#<1
#⮞ Data pizzerias.csv ⮜#@>2
pizzeriasDf = pd.read_csv('../pizzerias.csv')#<2


#⮞ ColumnHeaders  ⮜#@>3
# Pizzeria Name
# Location
# Specialty Pizza
# Price Range
# Rating
# Delivery Options
# Vegan Friendly
# Established Year
# Seating Capacity
# Website#<3

#Example 1: Get single column
#⮞ ColumnGet Rating ⮜#@>4
rating = pizzeriasDf['Rating']#<4

#Example2: Get multiple columns

#⮞ ColumnGet Location Rating ⮜#@>5
location = pizzeriasDf['Location']
rating_1 = pizzeriasDf['Rating']#<5

