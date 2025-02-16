
import os 




# Example 1
# mv is similar to the linux / mac / powershell
# mv command. In this example, we will move a file,
# in this case an image, using the hard coded names
# of the existing and new file location.
#
# Seed being used: #> mv Image.Backup.jpg NewImage.jpg 
# ******************************************************
# ******************************************************

#> mv Image.Backup.jpg NewImage.jpg 
os.rename( 'Image.Backup.jpg', 'NewImage.jpg' ) 



# Example 2
# Move a folder using the names of the existing and new
# folder location.
#
# Seed being used: #> mv FinishedPages C:/Users/user1/Documents/Revisions/Pages/ 
# ******************************************************
# ******************************************************

#> mv FinishedPages C:/Users/user1/Documents/Revisions/Pages/ 
os.rename( 'FinishedPages', 'C:/Users/user1/Documents/Revisions/Pages/' ) 



# Example 3
# Move a file using variable instead of hardcoded names
#
# Seed being used: #> mv initialFile copyLocation 
# ******************************************************
# ******************************************************

initialFile = 'Data/save.json'
copyLocation = 'Backup/save.json'

#> mv initialFile copyLocation 
os.rename( initialFile, copyLocation ) 



# Example 4
# Move multiple files using a for loop
#
# Seed being used: #> mv originalFile newFile 
# ******************************************************
# ******************************************************

imageCount = 50
for i in range(imageCount):
    originalFile = f'DCIM_{i}.jpg'
    newFile = f'CameraImage{i}.jpg'
    #> mv originalFile newFile 
    os.rename( originalFile, newFile ) 

