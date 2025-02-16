


# Example 1
# print will use the Python print command to print a message
# to the terminal, but, Arctic Fox will also write the result
# of the print command into the file as a comment. In this
# example, we use the default behavior of print to print the
# value of the most recently set variable.
#
# Seed being used: #> print 
# ******************************************************
# ******************************************************

number1 = 10
number2 = 50
number3 = 100

#> print 
print(number3) #)1 
##*** 100



# Example 2
# Print the value instead of a specified variable, not the
# default of the most recently set variable.
#
# Seed being used: #> print 
# ******************************************************
# ******************************************************

#> print number1 
print(number1) #)2 
##*** 10



# Example 2
# Print a message written and the print seed will
# automatically perform the string interpolation.
#
# Seed being used: #> print 
# ******************************************************
# ******************************************************

#> print The numbers we have are number1 , number2 , and number3 
print(f"The numbers we have are {number1} , {number2} , and {number3}") #)3 
##*** The numbers we have are 10 , 50 , and 100


