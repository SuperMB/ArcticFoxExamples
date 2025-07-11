 
import pandas as pd
import numpy as np  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None) 



# Setup
# ******************************************************
# ******************************************************



# Example 1
# Join the most recent to dataframes on a column
# Seed being used: #> Join --column StoreId --join left 
# ******************************************************
# ******************************************************

#> Data stores.csv 
storesDf = pd.read_csv('stores.csv')
storesDf['DateOpened'] = pd.to_datetime(storesDf['DateOpened']) 

#> ColumnHeaders 
# StoreId
# Name
# Address
# DateOpened 

#> Visualize 
print(storesDf.head()) #)1 
##***    StoreId            Name                                       Address DateOpened
##*** 0        1  Blossom Bazaar            PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22
##*** 1        2    Petal Palace      6488 Cowan Ramp\r\nLake Amanda, NE 57036 2021-01-15
##*** 2        3  Floral Fantasy                  USNS Aguilar\r\nFPO AP 64210 2022-02-27
##*** 3        4  Daisy Delights  474 Michelle Lane\r\nWrightborough, ID 25025 2019-05-30
##*** 4        5   Lavender Lane   09609 Scott Knolls\r\nBriannafort, KY 92840 2017-09-10



#> Data sales.csv 
salesDf = pd.read_csv('sales.csv')
salesDf['SaleDate'] = pd.to_datetime(salesDf['SaleDate']) 

#> ColumnHeaders 
# SaleId
# CustomerId
# Flower
# Quantity
# TotalSale
# SaleDate
# StoreId 

#> Visualize 
print(salesDf.head()) #)2 
##***    SaleId  CustomerId  Flower  Quantity  TotalSale   SaleDate  StoreId
##*** 0       1          92   Daisy        14         71 2023-07-24        3
##*** 1       2         752  Violet        16         33 2023-09-29       13
##*** 2       3         468   Daisy         1         45 2023-04-09        8
##*** 3       4         552   Peony        19         85 2024-01-06       22
##*** 4       5         639   Daisy         2         15 2023-06-29       15


#> Join --column StoreId --join left --example 
# selected left  table: storesDf
# selected right table: salesDf
storesDfSalesDfJoin = pd.merge(storesDf, salesDf, on=['StoreId'], how='left') 

#> Visualize 
print(storesDfSalesDfJoin.head()) #)3 
##***    StoreId            Name                             Address DateOpened  SaleId  CustomerId         Flower  Quantity  TotalSale   SaleDate
##*** 0        1  Blossom Bazaar  PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22      15         575          Tulip        11          9 2023-10-22
##*** 1        1  Blossom Bazaar  PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22      39         540         Violet         1          7 2024-01-18
##*** 2        1  Blossom Bazaar  PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22      76         783  Chrysanthemum        20         91 2024-02-13
##*** 3        1  Blossom Bazaar  PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22      79         822          Peony         3          1 2023-12-04
##*** 4        1  Blossom Bazaar  PSC 7602, Box 0671\r\nAPO AA 91313 2021-12-22      80         819      Carnation        13         29 2023-11-05



# Example 2
# Join dataframes on a column and specify the dataframes
# Seed being used: #> Join --column StoreId --join left 
# ******************************************************
# ******************************************************

#> Join --leftTable salesDf --rightTable storesDf --column StoreId --join left --example 
salesDfStoresDfJoin = pd.merge(salesDf, storesDf, on=['StoreId'], how='left') 

#> Visualize 
print(salesDfStoresDfJoin.head()) #)4 
##***    SaleId  CustomerId  Flower  Quantity  TotalSale   SaleDate  StoreId            Name                                            Address DateOpened
##*** 0       1          92   Daisy        14         71 2023-07-24        3  Floral Fantasy                       USNS Aguilar\r\nFPO AP 64210 2022-02-27
##*** 1       2         752  Violet        16         33 2023-09-29       13     Lily Luxury  2516 Michael Mission\r\nPort Thomasport, PA 66481 2020-09-12
##*** 2       3         468   Daisy         1         45 2023-04-09        8    Orchid Oasis         49187 Phillip Flat\r\nVincentton, KS 63511 2014-06-24
##*** 3       4         552   Peony        19         85 2024-01-06       22       Poppy Pod  8455 Perry Vista Apt. 903\r\nSouth Charlotte, ... 2014-09-28
##*** 4       5         639   Daisy         2         15 2023-06-29       15  Gardenia Grove  593 Bradley Union Suite 302\r\nSmithfort, CA 4... 2017-10-30
