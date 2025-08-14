 
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



#> Pie --values Wins --exampleImage Pie1.png --exampleTitle Pie Chart with Default Binning --example When plotting a pie chart of a numeric column without specifying bins, a default of 5 equal-width bins is applied. This gives a quick distribution overview of the Wins column by grouping win counts into 5 ranges automatically. 
# --bins not specified for pie chart with numeric values, default of 5 will be used

values = pd.cut(nBADf['Wins'], bins=5).value_counts()
indices = [str(index) for index in values.index]
combinedIndices = [str(indices[i]) + ' - ' + str(round(value[1] * 100 / sum(values), 1)) + '%' for i, value in enumerate(values.items())]

plt.pie(values, labels=combinedIndices)

plt.title('Wins', fontsize=14, fontweight='bold')
plt.show() 

#> Pie --values Wins --bins 10 --exampleImage Pie2.png --exampleTitle Pie Chart with Specified Number of Bins --example You can increase granularity by specifying the number of bins. This example divides the Wins column into 10 evenly spaced bins to provide a more detailed breakdown of the data distribution. 
values_1 = pd.cut(nBADf['Wins'], bins=10).value_counts()
indices_1 = [str(index) for index in values_1.index]
combinedIndices_1 = [str(indices_1[i]) + ' - ' + str(round(value[1] * 100 / sum(values_1), 1)) + '%' for i, value in enumerate(values_1.items())]

plt.pie(values_1, labels=combinedIndices_1)

plt.title('Wins', fontsize=14, fontweight='bold')
plt.show() 

#> Pie --values Wins --bins 0 20 30 40 50 100 --exampleImage Pie3.png --exampleTitle Pie Chart with Custom Bin Ranges --example Instead of relying on equal-sized bins, you can define custom bin ranges that reflect domain-specific thresholds. In this example, the Wins column is bucketed into defined intervals that reflect milestone win totals. 
values_2 = pd.cut(nBADf['Wins'], bins=[0, 20, 30, 40, 50, 100]).value_counts()
indices_2 = [str(index) for index in values_2.index]
combinedIndices_2 = [str(indices_2[i]) + ' - ' + str(round(value[1] * 100 / sum(values_2), 1)) + '%' for i, value in enumerate(values_2.items())]

plt.pie(values_2, labels=combinedIndices_2)

plt.title('Wins', fontsize=14, fontweight='bold')
plt.show() 


#> Pie --values Team --exampleImage Pie4.png --exampleTitle Pie Chart of Categorical Values --example When using a categorical column such as Team, the pie chart shows the count of each unique value. This example groups by team name and shows how frequently each team appears in the dataset. Unsurprisingly, each team has roughly the same number of players. 
values_3 = nBADf['Team'].astype('category').cat.codes.value_counts().values
indices_3 = nBADf['Team'].astype('category').cat.codes.value_counts().index
pieChartLabels = nBADf['Team'].unique()
combinedIndices_3 = [str(pieChartLabels[i]) + ' - ' + str(round(values_3[i] * 100 / sum(values_3), 1)) + '%' for i in range(len(values_3))]

plt.pie(values_3, labels=combinedIndices_3)

plt.title('Team', fontsize=14, fontweight='bold')
plt.show() 

#> Pie --values Points --group Team --exampleImage Pie5.png --exampleTitle Pie Chart of Aggregated Values by Group --example This example uses the group option to sum the Points for each team. The pie chart then displays total points scored by each team, allowing you to compare their overall offensive output visually. 
nBADfGroup = nBADf.groupby('Team')['Points'].sum()
nBADfGroup = nBADfGroup.sort_values()
pieLabels = [f'{name}: {value}' for name, value in zip(nBADfGroup.index, nBADfGroup)]

if (nBADfGroup <= 0).all():
    nBADfGroup *= -1

plt.pie(nBADfGroup, labels=pieLabels)

colorCycleIndex = (colorCycleIndex + 1) % len(colorCycle)

plt.title('Points', fontsize=14, fontweight='bold')
plt.show() 



