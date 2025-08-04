 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_bool_dtype  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)  
plt.style.use("darktheme.mplstyle")
colorCycle = plt.rcParams['axes.prop_cycle'].by_key()['color']  
colorCycleIndex = 0 


#> Data Pokemon.csv 
pokemonDf = pd.read_csv('Pokemon.csv') 


#> View 
print(pokemonDf.head()) #)1 
##***    Number                   Name  Type1   Type2  Total  HP  Attack  Defense  Sp.Atk  Sp.Def  Speed  Generation  Legendary
##*** 0       1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45           1      False
##*** 1       2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60           1      False
##*** 2       3               Venusaur  Grass  Poison    525  80      82       83     100     100     80           1      False
##*** 3       3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80           1      False
##*** 4       4             Charmander   Fire     NaN    309  39      52       43      60      50     65           1      False

#> BoxPlot --exampleTitle Create Boxplots of All Numeric Columns --example Use a boxplot to quickly understand the distribution of each numeric column in the dataframe. This example automatically creates a single boxplot for each numeric column, all plotted together on one figure for easy comparison.
xTickIndex = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        plt.boxplot(pokemonDf[boxplotColumn], patch_artist=True, positions=[xTickIndex], labels=[boxplotColumn])
        xTickIndex += 1

plt.title('pokemonDf', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> BoxPlot --separate --exampleTitle Create Separate Boxplot Axis for Each Numeric Column --example Instead of plotting all numeric columns in a single axis, this example generates a dedicated subplot for each numeric column. This layout allows you to see each distribution more clearly and avoids plots having vastly different ranges when there are many numeric fields.
nonNumericColumnCount = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        nonNumericColumnCount += 1

_, boxplotAxes = plt.subplots(nrows=1, ncols=nonNumericColumnCount, figsize=(10, 5))
xTickIndex = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        boxplotAxes[xTickIndex].boxplot(pokemonDf[boxplotColumn], patch_artist=True, positions=[0], labels=[boxplotColumn])
        xTickIndex += 1

plt.suptitle('pokemonDf', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> BoxPlot --x Attack Defense Sp.Atk Sp.Def --exampleTitle Create Boxplots for Selected Columns --example Rather than plotting all numeric columns, this example focuses only on a specified subset: Attack, Defense, Sp.Atk, and Sp.Def. These boxplots help us compare the variability and central tendencies of key Pokemon battle attributes.
plt.boxplot(pokemonDf['Attack'], patch_artist=True, positions=[0], labels=['Attack'])

plt.boxplot(pokemonDf['Defense'], patch_artist=True, positions=[1], labels=['Defense'])

plt.boxplot(pokemonDf['Sp.Atk'], patch_artist=True, positions=[2], labels=['Sp.Atk'])

plt.boxplot(pokemonDf['Sp.Def'], patch_artist=True, positions=[3], labels=['Sp.Def'])

plt.title('Attack, Defense, Sp.Atk, and Sp.Def', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> BoxPlot --x Attack Defense Sp.Atk Sp.Def --separate --exampleTitle Create Separate Boxplot Axis for Selected Columns --example This example combines selective plotting with individual subplots, allowing us to view the distribution of specific columns (Attack, Defense, Sp.Atk, and Sp.Def) each in its own axis. This makes detailed comparison easier, especially when columns vary in scale or spread.
_, boxplotAxes = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))
boxplotAxes[0].boxplot(pokemonDf['Attack'], patch_artist=True, positions=[0])
boxplotAxes[0].set_xticks([0], ['Attack'])

boxplotAxes[1].boxplot(pokemonDf['Defense'], patch_artist=True, positions=[0])
boxplotAxes[1].set_xticks([0], ['Defense'])

boxplotAxes[2].boxplot(pokemonDf['Sp.Atk'], patch_artist=True, positions=[0])
boxplotAxes[2].set_xticks([0], ['Sp.Atk'])

boxplotAxes[3].boxplot(pokemonDf['Sp.Def'], patch_artist=True, positions=[0])
boxplotAxes[3].set_xticks([0], ['Sp.Def'])

plt.suptitle('Attack, Defense, Sp.Atk, and Sp.Def', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 


