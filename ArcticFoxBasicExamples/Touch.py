
import time
import os 



# Example 1
# Touch creates a new file or updates the timestamp on a
# file, similar to the linux / mac / powershell command
# touch. In this example, we touch a file named new1.txt. 
# The use for this seed is a bit more niche for people
# that want to use familiar linux style commands.
#
# Seed being used: #> touch new1.txt 
# ******************************************************
# ******************************************************

#> touch new1.txt 
if os.path.exists( 'new1.txt' ):
    current_time = time.time()
    os.utime( 'new1.txt', (current_time, current_time))
else:
    open( 'new1.txt' , 'w').close() 
