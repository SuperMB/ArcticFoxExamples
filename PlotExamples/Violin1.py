from pandas.api.types import is_bool_dtype
 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype  
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

#> Violin --exampleTitle --example 
xTickIndex = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        plt.violinplot(pokemonDf[boxplotColumn],  positions=[xTickIndex])
        xTickIndex += 1

xTicks = []
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        xTicks.append(boxplotColumn)

plt.gca().set_xticklabels(xTicks)
plt.gca().set_xticks(range(len(xTicks)))

plt.title('pokemonDf', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major')
plt.show() 

#> Violin --separate --exampleTitle --example
nonNumericColumnCount = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        nonNumericColumnCount += 1

_, boxplotAxes = plt.subplots(nrows=1, ncols=nonNumericColumnCount, figsize=(10, 5))
xTickIndex = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        boxplotAxes[xTickIndex].violinplot(pokemonDf[boxplotColumn],  positions=[0])
        xTickIndex += 1

xTickIndex = 0
for i, boxplotColumn in enumerate(pokemonDf.columns):
    if is_numeric_dtype(pokemonDf[boxplotColumn]) and not is_bool_dtype(pokemonDf[boxplotColumn]):
        boxplotAxes[xTickIndex].set_xticklabels([boxplotColumn])
        boxplotAxes[xTickIndex].set_xticks([0])
        xTickIndex += 1

plt.suptitle('pokemonDf', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major')
plt.show() 

#> Violin --x Attack Defense Sp.Atk Sp.Def --exampleTitle --example
plt.violinplot(pokemonDf['Attack'],  positions=[0])

plt.violinplot(pokemonDf['Defense'],  positions=[1])

plt.violinplot(pokemonDf['Sp.Atk'],  positions=[2])

plt.violinplot(pokemonDf['Sp.Def'],  positions=[3])

xTickLabels = ['Attack', 'Defense', 'Sp.Atk', 'Sp.Def']
plt.gca().set_xticklabels(xTickLabels)
plt.gca().set_xticks(range(len(xTickLabels)))

plt.title('Attack, Defense, Sp.Atk, and Sp.Def', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major')
plt.show() 

#> Violin --x Attack Defense Sp.Atk Sp.Def --separate --exampleTitle --example
_, boxplotAxes = plt.subplots(nrows=1, ncols=4, figsize=(10, 5))
boxplotAxes[0].violinplot(pokemonDf['Attack'],  positions=[0])
boxplotAxes[0].set_xticks([0], ['Attack'])

boxplotAxes[1].violinplot(pokemonDf['Defense'],  positions=[0])
boxplotAxes[1].set_xticks([0], ['Defense'])

boxplotAxes[2].violinplot(pokemonDf['Sp.Atk'],  positions=[0])
boxplotAxes[2].set_xticks([0], ['Sp.Atk'])

boxplotAxes[3].violinplot(pokemonDf['Sp.Def'],  positions=[0])
boxplotAxes[3].set_xticks([0], ['Sp.Def'])

plt.suptitle('Attack, Defense, Sp.Atk, and Sp.Def', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major')
plt.show() 

