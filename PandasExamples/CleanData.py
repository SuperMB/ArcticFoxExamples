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


#Example 1 removing missing data from the dataframe
#⮞ CleanData --removeMissing   ⮜#@>4
pizzeriasDf = pizzeriasDf.dropna()#<4

# Example 2 Fill missing Ratiing Delivery with mean of the column
#⮞ CleanData Rating  Delivery --fill Rating  Delivery --mean ⮜ #⮞ `> ⮜#@>5
pizzeriasDf[ ['Rating Delivery'] ] = pizzeriasDf[ ['Rating Delivery'] ].apply(lambda col: col.fillna(col.mean()))#<5

#⮞ print  ⮜#@>6
print(pizzeriasDf) ##1#<6

