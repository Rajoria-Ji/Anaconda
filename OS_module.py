import os

#select the directory whose content you want to list 
directory_path = "/usr"

#use the os module to list the directory content 
contents = os.listdir(directory_path)

print(contents)
