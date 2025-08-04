 
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

#> Histogram --x High --exampleTitle Plot Histogram of Single Column --example A histogram is useful to see how values are distributed across a column. In this example, we plot the histogram of the High column to observe the distribution of daily high prices in the Apple stock dataset. 
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

#> Histogram --x HighDivLow --exampleTitle Plot Histogram of Computed Ratio Column --example You can plot histograms of computed columns the same way as standard columns. Here we first compute the HighDivLow ratio by dividing the High column by the Low column, then plot a histogram to analyze how this ratio varies across the dataset. 
plt.hist(appleStockDf['HighDivLow'], bins=10)

plt.title('HighDivLow Histogram', fontsize=14, fontweight='bold')
plt.xlabel('HighDivLow', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Histogram --x Date --exampleTitle Plot Histogram of Dates --example Although histograms are typically used for numeric data, you can also visualize how dates are distributed in a dataset. This example shows how the Apple stock data is spread across time by plotting a histogram of the Date column. Unsurprisingly, the data is roughly evenly distributed according to the dates as the stock was traded daily during the week. 
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date'])

plt.hist(appleStockDf['Date'], bins=10)

plt.title('Date Histogram', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Counts', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 


#> Histogram --x Volume --bins 50 --exampleTitle Plot Histogram with Custom Bin Count --example You can specify the number of bins in a histogram to increase granularity. Here, we use 50 bins to better understand the distribution of trading Volume in the Apple stock data, revealing more detail than the default setting. 
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

#> Histogram --x Attack Sp.Atk Defense Sp.Def --bins 20 --exampleTitle Compare Distributions of Multiple Columns --example When comparing the distributions of several related columns, you can overlay multiple histograms on the same plot. In this case, we compare Attack, Sp.Atk, Defense, and Sp.Def from the Pokemon dataset, using the same bin count to observe their relative distributions.
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
