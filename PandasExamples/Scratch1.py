
import os 



#> pwd 
pwd = os.getcwd() 

#> print 
print(pwd) #)1 
##*** c:\Users\littl\Code\GitHub\ArcticFoxExamples\PandasExamples

#> cd ../.af/ 
os.chdir( '../.af/' ) 

#> cd New  folder 
os.chdir( 'New folder' ) 

#> ls --print 
ls = os.listdir()
print(ls) #)2 
##*** ['pandasexamples_changecells.linemap.json', 'pandasexamples_cleandata.linemap.json', 'pandasexamples_columnadd.linemap.json', 'pandasexamples_columnaverage.linemap.json', 'pandasexamples_columncast.linemap.json', 'pandasexamples_columncombine.linemap.json', 'pandasexamples_columnconvert.linemap.json', 'pandasexamples_columnconvert2.linemap.json', 'pandasexamples_columncopy.linemap.json', 'pandasexamples_columncorrelation.linemap.json', 'pandasexamples_columndatatypes.linemap.json', 'pandasexamples_columnextract.linemap.json', 'pandasexamples_columnfor.linemap.json', 'pandasexamples_columnget.linemap.json', 'pandasexamples_columnheaders.linemap.json', 'pandasexamples_columnmax.linemap.json', 'pandasexamples_columnmean.linemap.json', 'pandasexamples_columnmedian.linemap.json', 'pandasexamples_columnmin.linemap.json', 'pandasexamples_columnmode.linemap.json', 'pandasexamples_columnop.linemap.json', 'pandasexamples_columnquantile.linemap.json', 'pandasexamples_columnrearrange.linemap.json', 'pandasexamples_columnremove.linemap.json', 'pandasexamples_columnrename.linemap.json', 'pandasexamples_columnround.linemap.json', 'pandasexamples_columnstandarddeviation.linemap.json', 'pandasexamples_columnsum.linemap.json', 'pandasexamples_columnunique.linemap.json', 'pandasexamples_columnvariance.linemap.json', 'pandasexamples_data.linemap.json', 'pandasexamples_dataframeconcat.linemap.json', 'pandasexamples_dataframecopy.linemap.json', 'pandasexamples_dataframedescribe.linemap.json', 'pandasexamples_dataframeequal.linemap.json', 'pandasexamples_dataframepivot.linemap.json', 'pandasexamples_dataframesave.linemap.json', 'pandasexamples_dataframeshuffle.linemap.json', 'pandasexamples_dataframesjoin.linemap.json', 'pandasexamples_focus.linemap.json', 'pandasexamples_normalize.linemap.json', 'pandasexamples_query.linemap.json', 'pandasexamples_randomdataframe.linemap.json', 'pandasexamples_removeweirdcharacters.linemap.json', 'pandasexamples_resetindexes.linemap.json', 'pandasexamples_rowcategorize.linemap.json', 'pandasexamples_rowcount.linemap.json', 'pandasexamples_rowduplicates.linemap.json', 'pandasexamples_rowfor.linemap.json', 'pandasexamples_rowget.linemap.json', 'pandasexamples_rowremove.linemap.json', 'pandasexamples_rowsort.linemap.json', 'pandasexamples_rowsum.linemap.json', 'pandasexamples_toseries.linemap.json', 'pandasexamples_visualize.linemap.json', 'pandasexamples_visualizeallcolumns.linemap.json', 'pandasexamples_visualizeallrows.linemap.json', 'pandasexamples_visualizedefaults.linemap.json']

#MBHERE TRYING TO RENAME THE LINE MAP FILES FOR EXAMPLES

for file in ls:
    newFile = file.replace('pandasexamples_', 'pandasexamples_exampleswithseedsonly_')
    #> mv file newFile 
    #ISSUE: DependsOn() takes exactly 1 argument (0 given) 

