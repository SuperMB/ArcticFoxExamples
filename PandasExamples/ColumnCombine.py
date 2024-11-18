#>1
import pandas as pd
import numpy as np#<1

#⮞ Data Pizzerias.csv ⮜#@>2
pizzeriasDf = pd.read_csv('../Pizzerias.csv')#<2

# what is this supposed to do?
# MB Refactor
#⮞ ColumnCombine Pizzeria  Name Location --keepNonNull  ⮜#@>3
pizzeriasDf['Pizzeria Name'] = pizzeriasDf['Pizzeria Name'].combine_first(pizzeriasDf['Location'])
pizzeriasDf = pizzeriasDf.drop(columns='Location')#<3

