


# Example 1
# Read is designed to work with different file types to load
# them into your Python script. Currently, text files, csvs,
# and images are supported. This list will grow over time.
#
# Write, similarly, saves data to files based on the save
# file's extensions type.
#
# This example shows reading in an email, which is a text file,
# and changing the <NAME> to a Greg's name. Then, we save
# the result to greg_email.txt. Lastly, we read the resulting
# file and see that the name was changed as desired.
#
# Seed being used:
# 1) #> Read email.txt 
# 2) #> write emailText greg_email.txt 
# ******************************************************
# ******************************************************

emailText = open('email.txt', "r").read() #< Read email.txt 

#> print 
print(emailText) #)1 
##*** Hey <NAME>,
##***
##*** Hope you're doing well! I was thinking it'd be great to catch up, want to meet at Starbucks at 10 AM? Let me know if that works for you or if another time is better.
##***
##*** Looking forward to it!
##***
##*** Cheers,
##*** Michael


emailText = emailText.replace('<NAME>', 'Greg')

#> write emailText greg_email.txt 
with open('greg_email.txt', 'w') as file:
    file.write(str(emailText)) 

checkEmailText = open('greg_email.txt', "r").read() #< Read greg_email.txt 

#> print 
print(checkEmailText) #)2 
##*** Hey Greg,
##***
##*** Hope you're doing well! I was thinking it'd be great to catch up, want to meet at Starbucks at 10 AM? Let me know if that works for you or if another time is better.
##***
##*** Looking forward to it!
##***
##*** Cheers,
##*** Michael
