 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)  
plt.style.use("darktheme.mplstyle")
colorCycle = plt.rcParams['axes.prop_cycle'].by_key()['color']  
colorCycleIndex = 0 

#> Data NBA.csv 
nBADf = pd.read_csv('NBA.csv') 

#> View 
print(nBADf.head()) #)1 
##***                     Player Team  Age  GamesPlayed  Wins  Losses     Min  Points  FGM   FGA  FG_Percent  3PM  3PA  3P_Percent  FTM  FTA   FT%  OREB  DREB  REB  AST  TOV  STL  BLK   PF    FP  DD2  TD3  PlusMinus
##*** 0  Shai Gilgeous-Alexander  OKC   26           70    59      11  2401.8    2301  795  1522        52.2  148  400        37.0  563  625  90.1    60   293  353  440  175  123   71  153  3792    5    0        861
##*** 1          Anthony Edwards  MIN   23           71    41      30  2566.6    1932  636  1444        44.0  283  716        39.5  377  449  84.0    56   349  405  325  227   81   42  127  3048    6    0        218
##*** 2             Nikola Jokic  DEN   30           64    43      21  2332.5    1872  714  1244        57.4  121  294        41.2  323  402  80.3   186   634  820  653  209  113   43  145  4095   54   30        541
##*** 3    Giannis Antetokounmpo  MIL   30           60    34      26  2039.2    1814  714  1189        60.1    9   50        18.0  377  624  60.4   138   579  717  357  191   50   72  149  3385   49    7        235
##*** 4             Jayson Tatum  BOS   27           66    48      18  2403.5    1791  612  1345        45.5  236  670        35.2  331  409  80.9    44   529  573  393  198   73   34  145  3191   29    2        490

#> Scatter --x Age --y Points 
plt.scatter(nBADf['Age'], nBADf['Points'], color=colorCycle[colorCycleIndex], label='Points')

plt.title('Points vs Age', fontsize=14, fontweight='bold')
plt.xlabel('Age', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Points', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
  

#> BestFitLine  --x Age --y Points --samePlot --exampleTitle Add a Best Fit Line to Scatter Plot --example After plotting two variables on a scatter plot, it is often useful to include a best fit line to help visualize the overall trend. In this example, we fit a line to the relationship between player Age and Points, and display it on the same plot to highlight the directional correlation in the data.
colorCycleIndex = colorCycleIndex + 1

coefficients = np.polyfit(nBADf['Age'], nBADf['Points'], 1)
p = np.poly1d(coefficients)
x_fit = np.linspace( ( nBADf['Age'] ).min(), ( nBADf['Age'] ).max(), 100)
y_fit = p(x_fit)
plt.plot(x_fit, y_fit, label=f'{coefficients[0]:.3f}x + {coefficients[1]:.3f}', color=colorCycle[colorCycleIndex])

plt.legend()
plt.show() 

# #> RowCategorize --columns Age --categories LessThan20 < 20, 20-30 < 30, 30-40 < 40, 40-50 < 50, Over50 
# #> ColumnRename --columns AgeCategorized --to AgeRanges 

# #> Scatter --x FG_Percent --y Wins --group AgeRanges 

# #> BestFitLine --x FG_Percent --y Wins --group AgeRanges --samePlot 



