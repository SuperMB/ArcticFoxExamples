 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype  
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


#> BoxPlot --exampleTitle --example
xTickIndex = 0
for i, boxplotColumn in enumerate(appleStockDf.columns):
    if is_numeric_dtype(appleStockDf[boxplotColumn]):
        plt.boxplot(appleStockDf[boxplotColumn], patch_artist=True, positions=[xTickIndex], labels=[boxplotColumn])
        xTickIndex += 1

plt.title('appleStockDf', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

