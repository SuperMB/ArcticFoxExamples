
import os 



# Example 1
# mkdir acts similar to the linux / mac / powershell mkdir
# command that creates a new folder. This example shows
# how to make a folder relative to the current path.
#
# Seed being used: #> mkdir datasets 
# ******************************************************
# ******************************************************

#> mkdir datasets 
if not os.path.exists('datasets'):
    os.makedirs('datasets') 




# Example 2
# This example shows how to make a folder using the new
# folder's full path.
#
# Seed being used: #> mkdir /home/john/code/school/projects/february/ 
# ******************************************************
# ******************************************************

#> mkdir /home/john/code/school/projects/february/ 
if not os.path.exists('/home/john/code/school/projects/february/'):
    os.makedirs('/home/john/code/school/projects/february/') 


