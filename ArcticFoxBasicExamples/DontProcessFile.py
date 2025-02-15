


# Example 1
# DontProcessFile prevents and seeds in the file from running.
# In this example, the seeds before and after DontProcessFile
# are not processed and do not write code
#
# Seed being used: #> DontProcessFile 
# ******************************************************
# ******************************************************

#> mv Image1.jpg OldImage1.jpg 

#> DontProcessFile 

#> mv NewImage.jpg Image1.jpg 

