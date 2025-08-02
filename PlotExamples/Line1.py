 
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)  
plt.style.use("darktheme.mplstyle")
colorCycle = plt.rcParams['axes.prop_cycle'].by_key()['color']  
colorCycleIndex = 0 

# Setup
# ******************************************************
# ******************************************************

#> Data AppleStock.csv 
appleStockDf = pd.read_csv('AppleStock.csv')
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date']) 


#> ColumnOp _HighMinusLow_ = _High_ - _Low_ 
appleStockDf['HighMinusLow'] = appleStockDf['High'] - appleStockDf['Low'] 

#> ColumnAdd --newColumnNames CloseVsOpen 
appleStockDf['CloseVsOpen'] = pd.Series() 


#> ExtractDate --columns Date --year 
appleStockDf['Date_Year'] = appleStockDf['Date'].dt.year 
#> ColumnRename --columns Date_Year --to Year 
appleStockDf = appleStockDf.rename(columns={'Date_Year': 'Year'}) 


#> RowCategorize --columns Year --categories 80s < 1990, 90s < 2000, 00s < 2010, 10s < 2020, 20s 
appleStockDf['YearCategorized'] = pd.cut(x=appleStockDf['Year'], bins=[-sys.maxsize,1990,2000,2010,2020,sys.maxsize], labels=['80s','90s','00s','10s','20s'], include_lowest=True) 
#> ColumnRename --columns YearCategorized --to Decade 
appleStockDf = appleStockDf.rename(columns={'YearCategorized': 'Decade'}) 


#> View 
print(appleStockDf.head()) #)1 
##***         Date      Open      High       Low     Close     Volume  HighMinusLow CloseVsOpen  Year Decade
##*** 0 1980-12-12  0.099058  0.099488  0.099058  0.099058  469033600      0.000431         NaN  1980    80s
##*** 1 1980-12-15  0.094321  0.094321  0.093890  0.093890  175884800      0.000431         NaN  1980    80s
##*** 2 1980-12-16  0.087429  0.087429  0.086999  0.086999  105728000      0.000431         NaN  1980    80s
##*** 3 1980-12-17  0.089152  0.089582  0.089152  0.089152   86441600      0.000431         NaN  1980    80s
##*** 4 1980-12-18  0.091737  0.092167  0.091737  0.091737   73449600      0.000431         NaN  1980    80s


# Examples
# ******************************************************
# ******************************************************

#> Line --x Date --y High --exampleImage Line1.png --exampleTitle Line Chart of a Numerical Column vs Date Column --example A simple and commonly used way to visualize stock data is by plotting a line chart of a value over time. In this example, we display the High column plotted against the Date to understand how the highest recorded stock prices changed over time. 
appleStockDf.sort_values( [ 'Date' ] )['Date'] = pd.to_datetime(appleStockDf.sort_values( [ 'Date' ] )['Date'])

plt.plot(appleStockDf.sort_values( [ 'Date' ] )['Date'], appleStockDf.sort_values( [ 'Date' ] )['High'], color=colorCycle[colorCycleIndex], label='High')

plt.title('High vs Date', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('High', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Line --x Date --y Volume --exampleImage Line2.png --where _Date_ >= 2023 --exampleTitle Line Chart With a Filtering Condition --example To narrow down the data to a more recent time period, this example filters the dataframe to only include rows where the Date is in or after the year 2023. Then we plot the Volume column against Date to visualize recent trading activity. 
appleStockDf['Date'] = pd.to_datetime(appleStockDf['Date'])
appleStockDfQueried = appleStockDf[appleStockDf['Date'].dt.year >= 2023]

appleStockDfQueried.sort_values( [ 'Date' ] )['Date'] = pd.to_datetime(appleStockDfQueried.sort_values( [ 'Date' ] )['Date'])

plt.plot(appleStockDfQueried.sort_values( [ 'Date' ] )['Date'], appleStockDfQueried.sort_values( [ 'Date' ] )['Volume'], color=colorCycle[colorCycleIndex], label='Volume')

plt.title('Volume vs Date, where Date >= 2023', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Volume', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Line --x High --y Volume --group Decade --exampleImage Line3.png --exampleTitle Line Chart Grouped by a Categorical Column --example Grouped visualizations help compare trends across categories. In this example, we group the data by Decade and plot Volume vs High for each group separately, using a different color for each decade to highlight changes in the relationship over time. 
appleStockDf['DecadeCategories'] = appleStockDf['Decade'].astype('category').cat.codes
for decadeIndex, decadeValue in enumerate(appleStockDf['Decade'].unique()):
    groupedRows = appleStockDf[appleStockDf['Decade'] == decadeValue]    

    plt.plot(groupedRows.sort_values( [ 'High' ] )['High'], groupedRows.sort_values( [ 'High' ] )['Volume'], color=colorCycle[colorCycleIndex], label='Volume' + f" when Decade is {appleStockDf.sort_values( [ 'High' ] )['Decade'].astype('category').cat.categories[decadeIndex]}", alpha=0.7)    

    colorCycleIndex = (colorCycleIndex + 1) % len(colorCycle)
appleStockDf = appleStockDf.drop(['DecadeCategories'], axis=1)

plt.title('Volume vs High', fontsize=14, fontweight='bold')
plt.xlabel('High', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Volume', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Line --x Year --y High --max --where _Year_ >= 2020 --exampleImage Line4.png --exampleTitle Line Chart With Aggregation --example Instead of plotting every data point, this example aggregates the data by Year and calculates the maximum High value within each year. This is useful for summarizing and comparing peak values over time, especially when filtering for only recent years (2020 and later). 
appleStockDfQueried = appleStockDf[appleStockDf['Year'] >= 2020]

appleStockDfQueriedGroup = appleStockDfQueried.groupby(['Year'])['High']
appleStockDfQueriedGroupMax = appleStockDfQueriedGroup.max()
appleStockDfQueriedGroupMax = pd.DataFrame(appleStockDfQueriedGroupMax).reset_index(names=['Year'])

plt.plot(appleStockDfQueriedGroupMax['Year'], appleStockDfQueriedGroupMax['High'], color=colorCycle[colorCycleIndex], label='High' + ' - max')

plt.title('High vs Year, where Year >= 2020', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('High', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 


