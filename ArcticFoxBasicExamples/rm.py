
import os 



# Example 1
# rm removes files or folders similar to the linux / mac /
# powershell rm command. In this example, we remove a file
# using a hardcoded file name.
#
# Seed being used: #> rm data.old.csv 
# ******************************************************
# ******************************************************

#> rm data.old.csv 
os.remove( 'data.old.csv' ) 



# Example 2
# Remove a file using a file name stored in a variable.
#
# Seed being used: #> rm fileToRemove 
# ******************************************************
# ******************************************************

fileToRemove = 'FunnyCat.jpg'
#> rm fileToRemove 
os.remove( fileToRemove ) 



# Example 3
# Remove a folder with the -r flag for a hard coded path.
#
# Seed being used: #> rm -r images/saved/ 
# ******************************************************
# ******************************************************

#> rm -r images/saved/ 
os.rmdir( 'images/saved/' ) 



# Example 4
# Remove a folder with the -r flag for a path in a variable
# using a for loop.
#
# Seed being used: #> rm -r pathToRemove 
# ******************************************************
# ******************************************************

foldersToRemove = ['catsPics', 'dogPics', 'birdPics']

for folder in foldersToRemove:
    pathToRemove = 'C:/Users/local/Images/' + folder
    #> rm -r pathToRemove 
    os.rmdir( pathToRemove ) 
