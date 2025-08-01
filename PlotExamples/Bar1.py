 
import sys
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



#> RowCategorize --columns GamesPlayed --categories Few < 30, Average < 60, Many 
nBADf['GamesPlayedCategorized'] = pd.cut(x=nBADf['GamesPlayed'], bins=[-sys.maxsize,30,60,sys.maxsize], labels=['Few','Average','Many'], include_lowest=True) 

#> View 
print(nBADf.head()) #)1 
##***                     Player Team  Age  GamesPlayed  Wins  Losses     Min  Points  FGM   FGA  FG_Percent  3PM  3PA  3P_Percent  FTM  FTA   FT%  OREB  DREB  REB  AST  TOV  STL  BLK   PF    FP  DD2  TD3  PlusMinus GamesPlayedCategorized
##*** 0  Shai Gilgeous-Alexander  OKC   26           70    59      11  2401.8    2301  795  1522        52.2  148  400        37.0  563  625  90.1    60   293  353  440  175  123   71  153  3792    5    0        861                   Many
##*** 1          Anthony Edwards  MIN   23           71    41      30  2566.6    1932  636  1444        44.0  283  716        39.5  377  449  84.0    56   349  405  325  227   81   42  127  3048    6    0        218                   Many
##*** 2             Nikola Jokic  DEN   30           64    43      21  2332.5    1872  714  1244        57.4  121  294        41.2  323  402  80.3   186   634  820  653  209  113   43  145  4095   54   30        541                   Many
##*** 3    Giannis Antetokounmpo  MIL   30           60    34      26  2039.2    1814  714  1189        60.1    9   50        18.0  377  624  60.4   138   579  717  357  191   50   72  149  3385   49    7        235                Average
##*** 4             Jayson Tatum  BOS   27           66    48      18  2403.5    1791  612  1345        45.5  236  670        35.2  331  409  80.9    44   529  573  393  198   73   34  145  3191   29    2        490                   Many


#> Bar Age 
indexForPlot = range(len(nBADf['Age']))

plt.bar(indexForPlot, nBADf['Age'], color=colorCycle[colorCycleIndex], label='Age')

plt.title('Age vs Index', fontsize=14, fontweight='bold')
plt.xlabel('Index', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Age', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 


#> Bar --x Team --xCategorical --y Points --sum --exampleTitle Bar Graph By Summing a Column 
nBADfGroup = nBADf.groupby(['Team'])['Points']
nBADfGroupSum = nBADfGroup.sum()
nBADfGroupSum = pd.DataFrame(nBADfGroupSum).reset_index(names=['Team'])

plt.bar(nBADfGroupSum['Team'].astype('category').cat.codes, nBADfGroupSum['Points'], label='Points' + ' - sum')

plt.gca().set_xticklabels(nBADfGroupSum['Team'].astype('category').cat.categories, rotation=45)
plt.gca().set_xticks(range(len(nBADfGroupSum['Team'].astype('category').cat.categories)))

plt.title('Points vs Team', fontsize=14, fontweight='bold')
plt.xlabel('Team', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Points', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Bar --x Team --xCategorical  --count 
values = nBADf['Team'].astype('str').value_counts().sort_index().values
indices = nBADf['Team'].astype('str').value_counts().sort_index().index

plt.bar(indices, values, color=colorCycle[colorCycleIndex], label='Team' + ' - count')

plt.title("'Team' count", fontsize=14, fontweight='bold')
plt.ylabel('count', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Bar --x Losses --y Wins --mean 
nBADfGroup_1 = nBADf.groupby(['Losses'])['Wins']
nBADfGroup_1Mean = nBADfGroup_1.mean()
nBADfGroup_1Mean = pd.DataFrame(nBADfGroup_1Mean).reset_index(names=['Losses'])

barWidth = 0.8
plt.bar(nBADfGroup_1Mean['Losses'], nBADfGroup_1Mean['Wins'], barWidth, label='Wins' + ' - mean')

plt.title('Wins vs Losses', fontsize=14, fontweight='bold')
plt.xlabel('Losses', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Wins', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 

#> Bar --x Team --y Wins --group GamesPlayedCategorized --mean 
nBADf['TeamCategories'] = nBADf['Team'].astype('category').cat.codes
nBADf['GamesPlayedCategorizedCategories'] = nBADf['GamesPlayedCategorized'].astype('category').cat.codes
nBADfGroup_2 = nBADf.groupby(['TeamCategories', 'GamesPlayedCategorizedCategories'])['Wins']
groupedRowsMean = nBADfGroup_2.mean()
groupedRowsMean = pd.DataFrame(groupedRowsMean).reset_index(names=['Team', 'GamesPlayedCategorized'])

for gamesPlayedCategorizedIndex, gamesPlayedCategorizedValue in enumerate(groupedRowsMean['GamesPlayedCategorized'].unique()):
    groupedRows = groupedRowsMean[groupedRowsMean['GamesPlayedCategorized'] == gamesPlayedCategorizedValue]    

    num_bars = len(nBADf['GamesPlayedCategorized'].unique())
    barWidth =  .9 / num_bars    
    plt.bar(groupedRows['Team'] + gamesPlayedCategorizedIndex * barWidth - (num_bars - 1) * barWidth / 2, groupedRows['Wins'], barWidth, label='Wins' + ' - mean' + f" when GamesPlayedCategorized is {nBADf['GamesPlayedCategorized'].astype('category').cat.categories[gamesPlayedCategorizedIndex]}")    

    colorCycleIndex = (colorCycleIndex + 1) % len(colorCycle)
plt.gca().set_xticklabels(nBADf['Team'].astype('category').cat.categories)
plt.gca().set_xticks(range(len(nBADf['Team'].astype('category').cat.categories)))
nBADf = nBADf.drop(['TeamCategories', 'GamesPlayedCategorizedCategories'], axis=1)

plt.title('Wins vs Team', fontsize=14, fontweight='bold')
plt.xlabel('Team', fontsize=12, fontweight='bold', color='gray')
plt.ylabel('Wins', fontsize=12, fontweight='bold', color='gray')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show() 



