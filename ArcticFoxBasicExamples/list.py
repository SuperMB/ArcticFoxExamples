


# Example 1
# The list seed assists in creating new list objects. In
# this example, we create an empty list.
#
# Seed being used: #> list 
# ******************************************************
# ******************************************************

#> list 
myList = [] 



# Example 2
# Similar to Example 1, but this time, we specify the
# variable name for the empty list by placing the list
# seed on the right hand side of the equation.
#
# Seed being used: #> list 
# ******************************************************
# ******************************************************

secondList =  [] #< list 



# Example 3
# Create a list with a specified number of entries for
# the list to start with.
#
# Seed being used: #> list --count 100 
# ******************************************************
# ******************************************************

thirdList = [0] * 100 #< list --count 100 

#> print 
print(thirdList) #)1 

# the value of thirdList should be printed, it isn't for some reason


# Example 4
# Create a list with a specified number of entries for
# the list to start with and specfiying an equation to
# be used to evaluate the values of the list. In our case,
# for simplicity, we will square the index and add 20.
#
# Seed being used: #> list --equation i ** 2 + 20 --count 20 
# ******************************************************
# ******************************************************

equationList = [i ** 2 + 20 for i in range(20)] #< list --equation i ** 2 + 20 --count 20 

#> print equationList 
print(equationList) #)2 
##*** [20, 21, 24, 29, 36, 45, 56, 69, 84, 101, 120, 141, 164, 189, 216, 245, 276, 309, 344, 381]



