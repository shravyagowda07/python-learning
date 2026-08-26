#import os
#print("Current directory:")
#print(os.getcwd())
#print("\nFiles and Folders:")
#print(os.listdir())
#print(os.mkdir("Test"))
#print(os.mkdirs("Project/Python/Files"))
#print(os.path.exists("notes.txt"))
#print(os.path.isfile("student.txt"))
#print(os.path.isfile("MyFolder"))
#print(os.path.isdir("28_os Module"))
#print(os.rename("notes.txt", "my_notes.txt"))
#print(os.remove("my_notes.txt"))
#print(os.rmdir("Test"))


import os
#show current location
print("Current Folder:")
print(os.getcwd())

#show files and folders
print("\nFiles and folders:")
print(os.listdir())

#create a folder
folder = "Test_Folder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("\nTest_Folder created.")
else:
    print("\nTest_Folder already exists.")

#check whether it is a folder
print("Is it a folder?", os.path.isdir(folder))

#Rename the folder
new_folder = "My_Test_Folder"
if os.path.exists(folder):
    os.rename(folder, new_folder)
    print("Folder renamed.")

#Check the new folder
print("Does new folder exist?", os.path.exists(new_folder))

#Delete the empty folder
if os.path.isdir(new_folder):
    os.rmdir(new_folder)
    print("Folder deleted.")