import math
 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  
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

#> Scatter --x FG_Percent --y Points --exampleTitle Scatter Plot of Numerical Columns --example A basic scatter plot showing how many points each player scored relative to their field goal percentage. This type of chart visualizes whether more efficient shooters tend to score more points overall.
plt.scatter(nBADf['FG_Percent'], nBADf['Points'], color=colorCycle[colorCycleIndex], label='Points')

plt.title('Points vs FG_Percent', fontsize=14, fontweight='bold')
plt.xlabel('FG_Percent', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Points', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Scatter --x Team --y Age --exampleTitle Scatter Plot of Numerical vs Categorical Columns --example This scatter plot compares the age of each player by their team. The x-axis shows each team labels, while the y-axis shows player age. This examples identifies age distribution across teams.
plt.scatter(nBADf['Team'].astype('category').cat.codes, nBADf['Age'], color=colorCycle[colorCycleIndex], label='Age')

plt.gca().set_xticklabels(nBADf['Team'].astype('category').cat.categories, rotation=45)
plt.gca().set_xticks(range(len(nBADf['Team'].astype('category').cat.categories)))

plt.title('Age vs Team', fontsize=14, fontweight='bold')
plt.xlabel('Team', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Age', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Scatter Points --exampleTitle Scatter Plot by Index --example In this example, we visualize the Points column directly against its index. This creates a simple trend view of scoring across the dataset making it easy to see data across a single column.
indexForPlot = range(len(nBADf['Points']))

plt.scatter(indexForPlot, nBADf['Points'], marker='o', color=colorCycle[colorCycleIndex], label='Points')

plt.title('Points vs Index', fontsize=14, fontweight='bold')
plt.xlabel('Index', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Points', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Scatter --x Wins --y BLK AST FG_Percent --exampleTitle Scatter Plot of Multiple Columns --example We compare three different performance metrics — BLK, AST, and FG_Percent — against Wins. Each metric is plotted with a different color on the same scatter plot, making it easier to spot how these variables trend with team success.
plt.scatter(nBADf['Wins'], nBADf['BLK'], color=colorCycle[colorCycleIndex], label='BLK')

colorCycleIndex = (colorCycleIndex + 1) % len(colorCycle)

plt.scatter(nBADf['Wins'], nBADf['AST'], color=colorCycle[colorCycleIndex], label='AST')

colorCycleIndex = (colorCycleIndex + 1) % len(colorCycle)

plt.scatter(nBADf['Wins'], nBADf['FG_Percent'], color=colorCycle[colorCycleIndex], label='FG_Percent')

plt.title('BLK, AST, and FG_Percent vs Wins', fontsize=14, fontweight='bold')
plt.xlabel('Wins', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('BLK, AST, and FG_Percent', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Scatter --x Wins --y Losses --z Points --exampleTitle 3D Scatter Plot of Points vs Wins and Losses --example This 3D scatter plot visualizes how scoring (Points) varies with both Wins and Losses. It can reveal whether high-scoring players are concentrated on winning or losing teams, and whether there's a balanced relationship between all three metrics.
plt.axes(projection='3d')

plt.gca().scatter(nBADf['Wins'], nBADf['Losses'], nBADf['Points'], color=colorCycle[colorCycleIndex], label='Points')

plt.title('Points vs Losses and Wins', fontsize=14, fontweight='bold')
plt.xlabel('Wins', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Losses', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 
