
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

# Example 1: cast to string
#> ColumnCast Speciality  Pizza Established  Year --type string 
pizzeriasDf['Speciality Pizza'] = pizzeriasDf['Speciality Pizza'].astype('str')
pizzeriasDf['Established Year'] = pizzeriasDf['Established Year'].astype('str') 
pizzeriasDf['Speciality Pizza'] = pizzeriasDf['Speciality Pizza'].astype('str')
pizzeriasDf['Established Year'] = pizzeriasDf['Established Year'].astype('str')

# Example 2: cast to int
#> ColumnCast Rating --type int 
pizzeriasDf['Rating'] = pizzeriasDf['Rating'].astype('int') 
pizzeriasDf['Rating'] = pizzeriasDf['Rating'].astype('int')

# Example 3: cast to float
#> ColumnCast Seating  Capacity --type float 
pizzeriasDf['Seating Capacity'] = pizzeriasDf['Seating Capacity'].astype('float') 
pizzeriasDf['Seating Capacity'] = pizzeriasDf['Seating Capacity'].astype('float')
