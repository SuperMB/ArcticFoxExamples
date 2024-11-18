#>1
import pandas as pd
import numpy as np#<1

#⮞ Data Pizzerias.csv ⮜#@>2
pizzeriasDf = pd.read_csv('../Pizzerias.csv')#<2

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

#Example 1: Copy single column
#⮞ ColumnCopy Location --to new_location ⮜#@>4
pizzeriasDf['new_location'] = pizzeriasDf['Location']#<4

#Example 2: Copy multiple columns
#⮞ ColumnCopy Rating Website --to newRating newWebsite ⮜#@>5
pizzeriasDf['newRating'] = pizzeriasDf['Rating']
pizzeriasDf['newWebsite'] = pizzeriasDf['Website']#<5

#⮞ print  ⮜#@>6
print(pizzeriasDf) ##1#<6
