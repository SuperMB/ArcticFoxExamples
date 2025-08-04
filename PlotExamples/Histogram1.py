 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)  
plt.style.use("darktheme.mplstyle")
colorCycle = plt.rcParams['axes.prop_cycle'].by_key()['color']  
colorCycleIndex = 0 

#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 

#> View 
print(appleStockDf.head()) #)1 
##***         Date      Open      High       Low     Close     Volume
##*** 0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600
##*** 1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800
##*** 2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000
##*** 3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600
##*** 4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600

#> Histogram --x High 
plt.hist(appleStockDf['High'], bins=10)

plt.title('High Histogram', fontsize=14, fontweight='bold')
plt.xlabel('High', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> ColumnOp _HighDivLow_ = _High_ / _Low_ 
appleStockDf['HighDivLow'] = appleStockDf['High'] / appleStockDf['Low'] 

#> Histogram --x HighDivLow 
plt.hist(appleStockDf['HighDivLow'], bins=10)

plt.title('HighDivLow Histogram', fontsize=14, fontweight='bold')
plt.xlabel('HighDivLow', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Histogram --x Date 
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date'])

plt.hist(appleStockDf['Date'], bins=10)

plt.title('Date Histogram', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 


#> Histogram --x Volume --bins 50 
plt.hist(appleStockDf['Volume'], bins=50)

plt.title('Volume Histogram', fontsize=14, fontweight='bold')
plt.xlabel('Volume', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Data Pokemon.csv 
pokemonDf = pd.read_csv('Pokemon.csv') 

#> View 
print(pokemonDf.head()) #)2 
##***    Number                   Name  Type1   Type2  Total  HP  Attack  Defense  Sp.Atk  Sp.Def  Speed  Generation  Legendary
##*** 0       1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45           1      False
##*** 1       2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60           1      False
##*** 2       3               Venusaur  Grass  Poison    525  80      82       83     100     100     80           1      False
##*** 3       3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80           1      False
##*** 4       4             Charmander   Fire     NaN    309  39      52       43      60      50     65           1      False

#> Histogram --x Attack Sp.Atk Defense Sp.Def --bins 20 
plt.hist(pokemonDf['Attack'], bins=20, label='Attack', alpha=0.4)

plt.hist(pokemonDf['Sp.Atk'], bins=20, label='Sp.Atk', alpha=0.4)

plt.hist(pokemonDf['Defense'], bins=20, label='Defense', alpha=0.4)

plt.hist(pokemonDf['Sp.Def'], bins=20, label='Sp.Def', alpha=0.4)

plt.title('Attack, Sp.Atk, Defense, and Sp.Def Histogram', fontsize=14, fontweight='bold')
plt.xlabel('Attack, Sp.Atk, Defense, and Sp.Def', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 
