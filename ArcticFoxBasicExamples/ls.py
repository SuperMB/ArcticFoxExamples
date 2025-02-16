
import os 



# Example 1
# ls acts similar to the linux / mac / powershell ls command
# that get's a list of files and folders in the current
# folder. This example shows the default use of a simple
# ls seed that stores the list of files and folders in a
# variable called ls.
#
# Seed being used: #> ls 
# ******************************************************
# ******************************************************

#> ls 
ls = os.listdir() 



# Example 2
# Similar to Example 1, except that --print is used to
# display the resulting list of files and folders in the
# current folder.
#
# Seed being used: #> ls --print 
# ******************************************************
# ******************************************************

#> ls --print 
ls = os.listdir()
print(ls) #)1 
##*** ['.temp', 'cd.py', 'cp.py', 'DontProcessFile.py', 'Exists.py', 'for.py', 'GetType.py', 'HelloWorld.py', 'is.py', 'list.py', 'ls.py', 'mkdir.py', 'mv.py', 'PassThroughTemp.py', 'print.py', 'pwd.py', 'Random.py', 'Read.py', 'rm.py', 'Touch.py', 'Write.py']



# Example 3
# Similar to Example 1, except that the ls seed is on the
# right hand side of an equation, storing the result in the
# specified variable instead of a variable names ls.
#
# Seed being used: #> ls 
# ******************************************************
# ******************************************************

files = os.listdir() #< ls 



# Example 4
# A combination of exaples 2 and 3. A variable name is given
# on the left hand side of the equation and --print is used
# to print the list of files and folders.
#
# Seed being used: #> ls --print 
# ******************************************************
# ******************************************************

fileList = os.listdir() #< ls --print 
print(fileList) #)2 
##*** ['.temp', 'cd.py', 'cp.py', 'DontProcessFile.py', 'Exists.py', 'for.py', 'GetType.py', 'HelloWorld.py', 'is.py', 'list.py', 'ls.py', 'mkdir.py', 'mv.py', 'PassThroughTemp.py', 'print.py', 'pwd.py', 'Random.py', 'Read.py', 'rm.py', 'Touch.py', 'Write.py']

