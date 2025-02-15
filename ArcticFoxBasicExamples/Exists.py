
import os 



# Example 1
# Exists checks to see if a file or folder exists. This
# example shows checking to see if a file exists using a
# hardcoded file path relative to the current location.
#
# Seed being used: #> Exists csvs/names.csv 
# ******************************************************
# ******************************************************

#> Exists csvs/names.csv 
exists = os.path.exists('csvs/names.csv') 



# Example 2
# Check so see if a folder exists relative to the current
# location using a hardcoded path.
# Seed being used: #> Exists data/ 
# ******************************************************
# ******************************************************

#> Exists data/ 
exists = os.path.exists('data/') 



# Example 3
# Check so see if a file exists using a variable that
# contains the filename
# Seed being used: #> Exists data/ 
# ******************************************************
# ******************************************************

filePath = 'students/first_names.txt'
#> Exists filePath 
exists = os.path.exists(filePath) 



# Example 4
# Check so see if a file exists within an if statement
# Seed being used: #> Exists dates.json 
# ******************************************************
# ******************************************************

if os.path.exists('dates.json'):#< Exists dates.json 
    print('date file found')
