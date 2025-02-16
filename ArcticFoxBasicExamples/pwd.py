
import os 



# Example 1
# pwd gets the path that the interpreter is currently
# working in, similar to the pwd command in linux / mac /
# powershell. This example gets the current working directory
# and prints the value to the file. This is often used for
# debugging and making sure files are being accessed from the
# expected location.
#
# Seed being used: #> pwd --print 
# ******************************************************
# ******************************************************

#> pwd --print 
pwd = os.getcwd()
print(pwd) #)1 
##*** c:\Users\littl\Code\GitHub\ArcticFoxExamples\ArcticFoxBasicExamples



# Example 2
# Similar to Example 1, just showing that --print does not
# have to be used. Additionally, the result is set to a
# variable specified on the left hand side of the equation.
#
# Seed being used: #> pwd 
# ******************************************************
# ******************************************************

currentFolder = os.getcwd() #< pwd 


