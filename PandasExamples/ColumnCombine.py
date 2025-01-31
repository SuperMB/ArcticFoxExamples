
import pandas as pd
import numpy as np

#> Data Pizzerias.csv 
pizzeriasDf = pd.read_csv('Pizzerias.csv') 
pizzeriasDf = pd.read_csv('../Pizzerias.csv')

# what is this supposed to do?
# MB Refactor
#> ColumnCombine Pizzeria  Name Location --keepNonNull 
pizzeriasDf['Pizzeria Name'] = pizzeriasDf['Pizzeria Name'].combine_first(pizzeriasDf['Location'])
pizzeriasDf = pizzeriasDf.drop(columns='Location') 
pizzeriasDf['Pizzeria Name'] = pizzeriasDf['Pizzeria Name'].combine_first(pizzeriasDf['Location'])
pizzeriasDf = pizzeriasDf.drop(columns='Location')

