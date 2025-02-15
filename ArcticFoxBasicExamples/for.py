


# Example 1
# for provides a shortcut for writing for loops. In this
# example, for loops a specific number of times
#
# Seed being used: #> for 10 
# ******************************************************
# ******************************************************

#> for 10 
for i in range(10): 
    print(i)



# Example 2
# Loop from a starting to ending index
#
# Seed being used: #> for --start 20 --stop 30 
# ******************************************************
# ******************************************************

#> for --start 20 --stop 30 
for i in range(20, 30): 
    print(i)



# Example 3
# Loop over the last variable
#
# Seed being used: #> for 
# ******************************************************
# ******************************************************

values = [1, 2, 3,4 , 5]
#> for 
for value in values: 
    print(value)



# Example 4
# Loop over the a specified variable, and include
# the index of the loop
#
# Seed being used: #> for --start 20 --stop 30 
# ******************************************************
# ******************************************************

otherValues = [10, 11, 12, 13, 14]
#> for --source otherValues --useIndex 
for index, otherValue in enumerate(otherValues): 
    print(otherValue)