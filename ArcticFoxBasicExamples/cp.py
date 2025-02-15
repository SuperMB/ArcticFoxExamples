
import shutil 



# Example 1
# Copy a file, in this case an image, using the
# names of the existing and new files
# Seed being used: #> cp Image.Backup.jpg NewImage.jpg 
# ******************************************************
# ******************************************************

#> cp Image.Backup.jpg NewImage.jpg 
shutil.copy('Image.Backup.jpg', 'NewImage.jpg') 



# Example 2
# Copy a folder using the names of the existing and new folder
# Seed being used: #> cp -r FinishedPages C:/Users/user1/Documents/Revisions/Pages/ 
# ******************************************************
# ******************************************************

#> cp -r FinishedPages C:/Users/user1/Documents/Revisions/Pages/ 
shutil.copytree('FinishedPages', 'C:/Users/user1/Documents/Revisions/Pages/') 



# Example 3
# Copy a file using variable instead of hardcoded names
# Seed being used: #> cp initialFile copyLocation 
# ******************************************************
# ******************************************************

initialFile = 'Data/save.json'
copyLocation = 'Backup/save.json'

#> cp initialFile copyLocation 
shutil.copy(initialFile, copyLocation) 



# Example 4
# Copy multiple files using a for loop
# Seed being used: #> cp originalFile newFile 
# ******************************************************
# ******************************************************

imageCount = 50
for i in range(imageCount):
    originalFile = f'DCIM_{i}.jpg'
    newFile = f'CameraImage{i}.jpg'
    #> cp originalFile newFile 
    shutil.copy(originalFile, newFile) 

