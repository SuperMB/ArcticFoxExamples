

# Example 1
# is tests whether a variable is of a certain type. In this
# example, we check to see if myInteger is an integer, and
# print the result.
#
# Seed being used: #> is --type int 
# ******************************************************
# ******************************************************

myInteger = 5

#> is --type int 
myIntegerIs = isinstance(myInteger, int) 

#> print 
print(myIntegerIs) #)1 
##*** True



# Example 2
# This time, we check to see if myInteger from Example 1 is
# a float, which it is not, and will result to False. We also
# use --print in the is seed to show the result.
#
# Seed being used: #> is --type float --print 
# ******************************************************
# ******************************************************

myInteger = 10

#> is --type float --print 
myIntegerIs_1 = isinstance(myInteger, float)
print(myIntegerIs_1) #)2 
##*** False



# Example 3
# Checking the type of a variable in an if statement. Also,
# this example shows specifying the variable to check as opposed
# to using the last variable
#
# Seed being used: #> is  --variable myInteger --type int 
# ******************************************************
# ******************************************************

variableNotToTarget = 'Hello'

if isinstance(myInteger, int):#< is  --variable myInteger --type int 
    #> print myInteger is an int! 
    print(f"{myInteger} is an int!") #)3 
    ##*** 10 is an int!
else:
    #> print Not and int... 
    print(f"Not and int...") #)4 



