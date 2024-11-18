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

# Example 1: cast to string
#⮞ ColumnCast Speciality  Pizza Established  Year --type string ⮜#@>4
pizzeriasDf['Speciality Pizza'] = pizzeriasDf['Speciality Pizza'].astype('str')
pizzeriasDf['Established Year'] = pizzeriasDf['Established Year'].astype('str')#<4

# Example 2: cast to int
#⮞ ColumnCast Rating --type int ⮜#@>5
pizzeriasDf['Rating'] = pizzeriasDf['Rating'].astype('int')#<5

# Example 3: cast to float
#⮞ ColumnCast Seating  Capacity --type float ⮜#@>6
pizzeriasDf['Seating Capacity'] = pizzeriasDf['Seating Capacity'].astype('float')#<6
